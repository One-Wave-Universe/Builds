import unittest
import io,json,urllib.error
from unittest.mock import patch
import runner

class Gates(unittest.TestCase):
    def test_allowlisted_route_failure_is_visible(self):
        e=urllib.error.HTTPError('https://route.trycloudflare.com/chat',400,'Bad',{},io.BytesIO(json.dumps({'error':'DeepSeek output incomplete'}).encode()))
        with patch.object(runner.urllib.request,'urlopen',side_effect=e):
            with self.assertRaisesRegex(runner.GateError,'DeepSeek output incomplete'):runner.request_json(e.url)
    def test_arbitrary_server_error_is_not_echoed(self):
        e=urllib.error.HTTPError('https://route.trycloudflare.com/chat',400,'Bad',{},io.BytesIO(json.dumps({'error':'private credential content'}).encode()))
        with patch.object(runner.urllib.request,'urlopen',side_effect=e):
            with self.assertRaises(runner.GateError) as caught:runner.request_json(e.url)
        self.assertNotIn('private credential content',str(caught.exception))
    def req(self): return {"id":"test-1","repository":"One-Wave-Universe/Builds","question":"Check the build","actors":["GEMINI"]}
    def test_foreign_repository(self):
        x=self.req(); x["repository"]="someone/other"
        with self.assertRaises(runner.GateError): runner.validate(x)
    def test_bad_id(self):
        x=self.req(); x["id"]="../escape"
        with self.assertRaises(runner.GateError): runner.validate(x)
    def test_full_file_segmentation(self):
        text="abcdef"*40000
        chunks=runner.chunks_for([{"path":"all.md","git_blob":"x","text":text}],{})
        self.assertIn(text,"".join(chunks)); self.assertGreater(len(chunks),1)
    def test_truncated_tree_stops(self):
        with patch.object(runner,"gh",return_value={"truncated":True,"tree":[]}):
            with self.assertRaises(runner.GateError): runner.inventory("r","sha")
    def test_submodule_stops(self):
        with patch.object(runner,"gh",return_value={"truncated":False,"tree":[{"type":"commit"}]}):
            with self.assertRaises(runner.GateError): runner.inventory("r","sha")
    def test_budget_does_not_silently_shorten(self):
        scan=({"commit":"s"},[{"path":"all.md","git_blob":"s","text":"x"*(runner.CHUNK*2)}],{})
        with patch.object(runner,"scan",return_value=scan),patch.object(runner,"invoke") as model:
            x=self.req(); x["max_model_calls"]=1
            with self.assertRaises(runner.GateError):runner.cycle(x,"GEMINI",[])
            model.assert_not_called()
    def test_drift_rejects_answer(self):
        scan=({"commit":"old"},[{"path":"all.md","git_blob":"s","text":"hello"}],{})
        with patch.object(runner,"scan",return_value=scan),patch.object(runner,"invoke",return_value={"answer":"all.md","model":"m"}),patch.object(runner,"head",return_value="new"):
            with self.assertRaises(runner.GateError): runner.cycle(self.req(),"GEMINI",[])
    def test_missing_citation_rejects(self):
        scan=({"commit":"s"},[{"path":"all.md","git_blob":"s","text":"hello"}],{})
        with patch.object(runner,"scan",return_value=scan),patch.object(runner,"invoke",return_value={"answer":"unsupported","model":"m"}),patch.object(runner,"head",return_value="s"):
            with self.assertRaises(runner.GateError): runner.cycle(self.req(),"GEMINI",[])
    def test_peer_failure_does_not_stop_other_actor(self):
        def fake(req,actor,history):
            if actor=="GPT":raise runner.GateError("quota")
            return {"actor":actor,"answer":"ok","reference":{}}
        x=self.req();x["actors"]=["GPT","GEMINI"];x["cycles"]=2
        with patch.object(runner,"cycle",side_effect=fake),patch.object(runner,"publish"):
            r=runner.run(x)
        self.assertEqual(r["actors"]["GPT"]["status"],"HOLD")
        self.assertEqual(r["actors"]["GEMINI"]["cycles"],2)
        self.assertEqual(r["status"],"PARTIAL")
    def test_fast_actor_does_not_wait(self):
        import threading
        finished=threading.Event()
        def fake(req,actor,history):
            if actor=="GPT":
                if not finished.wait(2):raise AssertionError("Fast peer could not progress")
            elif len([t for t in history() if t["actor"]=="GEMINI"])==1: finished.set()
            return {"actor":actor,"answer":"ok","reference":{}}
        x=self.req();x["actors"]=["GPT","GEMINI"];x["cycles"]=2
        with patch.object(runner,"cycle",side_effect=fake),patch.object(runner,"publish"):
            r=runner.run(x)
        self.assertEqual(r["status"],"COMPLETE")
        self.assertEqual([t["actor"] for t in r["turns"]][:2],["GEMINI","GEMINI"])
    def test_any_registered_provider_gets_a_slot(self):
        x=self.req();x["actors"]=["TEST_PEER"]
        with patch.dict(runner.PROVIDERS,{"TEST_PEER":lambda *a: {"answer":"actual adapter call"}}):
            runner.validate(x)
            self.assertEqual(runner.invoke("TEST_PEER","system","question")["answer"],"actual adapter call")
    def test_all_blocked_is_hold(self):
        self.assertEqual(runner.overall_status({"a":{"status":"HOLD"},"b":{"status":"HOLD"}}),"HOLD")
    def test_metadata_is_read_by_every_requested_actor(self):
        scan=({'commit':'s'},[{'path':'all.md','git_blob':'s','text':'hello'}],{})
        x=self.req();x['metadata_queries']=[{'url':'https://gwosc.org/api/v2/runs','purpose':'test metadata'}]
        source={'provider':'GWOSC','source_record':{'retained_field':123},'sha256':'hash','worker':'Jetson'}
        for actor in ['GEMINI','GPT','DEEPSEEK']:
            with patch.object(runner,'scan',return_value=scan),patch.object(runner,'jetson',return_value=source),patch.object(runner,'invoke',return_value={'answer':'all.md','model':'m'}) as model,patch.object(runner,'head',return_value='s'):
                turn=runner.cycle(x,actor,[])
                self.assertEqual(turn['metadata_sources'][0]['source_record']['retained_field'],123)
                self.assertIn('retained_field',model.call_args_list[0].args[2])
    def test_metadata_rejects_private_target(self):
        x=self.req();x['metadata_queries']=[{'url':'https://127.0.0.1/api','purpose':'test'}]
        with self.assertRaises(runner.GateError):runner.validate(x)
    def test_incomplete_jetson_answer_rejected(self):
        with patch.object(runner,'jetson',return_value={'answer':'no receipt'}):
            with self.assertRaises(runner.GateError):runner.jetson_actor('DEEPSEEK','s','p')

if __name__=="__main__": unittest.main()
