import unittest
from unittest.mock import patch
import runner

class Gates(unittest.TestCase):
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
        self.assertEqual(r["status"],"HOLD")
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

if __name__=="__main__": unittest.main()
