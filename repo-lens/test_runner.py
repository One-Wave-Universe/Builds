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
    def source(self, repo):
        name=repo.split('/')[-1]
        text='SOURCE_'+name+(' TERMINAL_PROGRAM_ROUTE' if name=='Bridge-Comand' else '')
        return ({'repository':repo,'commit':'sha-'+name},[{'path':'same.md','git_blob':'blob-'+name,'text':text}],{'open_issues':[{'title':'ISSUE_'+name}]})
    def test_every_provider_reads_all_core_repos_and_terminal_routes(self):
        for actor in runner.PROVIDERS:
            with self.subTest(actor=actor),patch.object(runner,'scan',side_effect=self.source),patch.object(runner,'head',side_effect=lambda repo:'sha-'+repo.split('/')[-1]),patch.object(runner,'invoke',return_value={'answer':'Builds/same.md','response_id':'actual','model':'m'}) as model:
                turn=runner.cycle(self.req(),actor,[])
                supplied='\n'.join(call.args[2] for call in model.call_args_list)
                for name in runner.CORE_REPOS:
                    self.assertIn('SOURCE_'+name,supplied)
                    self.assertIn('ISSUE_'+name,supplied)
                self.assertIn('TERMINAL_PROGRAM_ROUTE',supplied)
                self.assertEqual(set(turn['reference']['repository_commits']),{runner.OWNER+'/'+name for name in runner.CORE_REPOS})
                self.assertEqual(turn['reference']['file_count'],3)
    def test_mythos_is_optional_and_focus_can_include_it(self):
        with patch.object(runner,'scan',side_effect=self.source):
            normal=runner.scan_all(runner.OWNER+'/Builds')[0]
            optional=runner.scan_all(runner.OWNER+'/Builds',True)[0]
            focus=runner.scan_all(runner.OWNER+'/Mythos-and-Stories')[0]
        self.assertNotIn(runner.OWNER+'/Mythos-and-Stories',normal['repository_commits'])
        self.assertIn(runner.OWNER+'/Mythos-and-Stories',optional['repository_commits'])
        self.assertEqual(optional['repository_commits'],focus['repository_commits'])
    def test_unreadable_secondary_repo_stops_before_any_model_call(self):
        def failing(repo):
            if repo.endswith('/One-Wave-Science'):raise runner.GateError('Science unavailable')
            return self.source(repo)
        with patch.object(runner,'scan',side_effect=failing),patch.object(runner,'invoke') as model:
            with self.assertRaisesRegex(runner.GateError,'Science unavailable'):runner.cycle(self.req(),'CLAUDE',[])
            model.assert_not_called()
    def test_drift_in_bridge_repo_rejects_completed_answer(self):
        def current(repo):return 'changed' if repo.endswith('/Bridge-Comand') else 'sha-'+repo.split('/')[-1]
        with patch.object(runner,'scan',side_effect=self.source),patch.object(runner,'head',side_effect=current),patch.object(runner,'invoke',return_value={'answer':'Builds/same.md','response_id':'actual'}):
            with self.assertRaisesRegex(runner.GateError,'Bridge-Comand'):runner.cycle(self.req(),'CLAUDE',[])
    def test_optional_flag_must_be_boolean(self):
        x=self.req();x['include_mythos']='yes'
        with self.assertRaises(runner.GateError):runner.validate(x)
    def test_index_preserves_every_path_and_avoids_repeated_bulk_data(self):
        repo=runner.OWNER+'/One-Wave-Science'
        files=[{'repository':repo,'path':'data.csv','git_blob':'a','bytes':2000000,'kind':'text','text':'1,2\n'*500000},{'repository':repo,'path':'AI_CANONICAL_START_HERE.md','git_blob':'b','bytes':15,'kind':'text','text':'CANON_REQUIRED'}]
        context,seeded=runner.indexed_context(files,{'repository_commits':{repo:'head'}})
        text=''.join(file['text'] for file in context)
        self.assertIn('data.csv',text);self.assertIn('CANON_REQUIRED',text)
        self.assertLess(len(text),len(files[0]['text'])//100)
        self.assertEqual(seeded,[repo+'/AI_CANONICAL_START_HERE.md'])
    def test_source_tool_returns_exact_verified_source(self):
        repo=runner.OWNER+'/Builds';file={'repository':repo,'path':'actual.py','git_blob':'sha','sha256':'hash','bytes':16,'kind':'text','text':'EXACT_FULL_SOURCE'}
        asks=[]
        def ask(prompt,stage):
            asks.append((prompt,stage))
            answer=json.dumps({'lens_tool':{'name':'get_repository_file','arguments':{'repository':repo,'path':'actual.py'}}}) if len(asks)==1 else 'actual.py verified'
            return {'answer':answer}
        audits=[]
        runner.lens_exchange('GPT','question',ask,[],[],audits.append,[file],{'repository_commits':{repo:'pinned'}})
        self.assertIn('EXACT_FULL_SOURCE',asks[1][0])
        self.assertEqual(audits[0]['commit'],'pinned')
    def test_source_tool_cannot_escape_verified_snapshot(self):
        def ask(*args):return {'answer':json.dumps({'lens_tool':{'name':'get_repository_file','arguments':{'repository':'other/repo','path':'../../secret'}}})}
        with self.assertRaisesRegex(runner.GateError,'outside current verified'):runner.lens_exchange('GPT','q',ask,[],[],files=[],evidence={})
    def test_metadata_tool_rejects_private_url_before_call(self):
        def ask(*args):return {'answer':json.dumps({'lens_tool':{'name':'query_metadata','arguments':{'url':'https://127.0.0.1/secrets','purpose':'test'}}})}
        with patch.object(runner,'jetson') as route:
            with self.assertRaises(runner.GateError):runner.lens_exchange('GPT','q',ask,[],[])
            route.assert_not_called()
    def test_each_adapter_can_query_metadata_as_a_real_tool(self):
        for actor in runner.PROVIDERS:
            with self.subTest(actor=actor):
                answers=iter([json.dumps({'lens_tool':{'name':'query_metadata','arguments':{'url':'https://gwosc.org/api/v2/runs','purpose':'read runs'}}}),'provider data read','final answer'])
                prompts=[];sources=[];audit=[]
                def ask(prompt,stage):prompts.append(prompt);return {'answer':next(answers)}
                value={'provider':'GWOSC','sha256':'real-receipt','source_record':{'preserved':123}}
                with patch.object(runner,'jetson',return_value=value) as route:runner.lens_exchange(actor,'question',ask,[],sources,audit.append)
                route.assert_called_once_with('/metadata',{'url':'https://gwosc.org/api/v2/runs','purpose':'read runs'})
                self.assertIn('preserved',prompts[1]);self.assertEqual(sources,[value])
    def test_peer_tool_returns_only_actual_completed_other_actor(self):
        peers=[{'actor':'GEMINI','cycle':1,'status':'COMPLETE','answer':'REAL_PEER_ANSWER','response_id':'peer-id'},{'actor':'GPT','cycle':1,'status':'COMPLETE','answer':'own'},{'actor':'GROK','status':'HOLD','answer':'not complete'}]
        answers=iter([json.dumps({'lens_tool':{'name':'get_peer_responses','arguments':{}}}),'peer read','final'])
        prompts=[]
        def ask(prompt,stage):prompts.append(prompt);return {'answer':next(answers)}
        runner.lens_exchange('GPT','q',ask,lambda:peers,[])
        self.assertIn('REAL_PEER_ANSWER',prompts[1]);self.assertNotIn('not complete',prompts[1])
    def test_tool_requests_have_a_finite_stop(self):
        def ask(prompt,stage):return {'answer':'read' if stage=='tool-result' else json.dumps({'lens_tool':{'name':'get_peer_responses','arguments':{}}})}
        with self.assertRaisesRegex(runner.ReReferenceRequired,'Repeated completed'):runner.lens_exchange('GPT','q',ask,[],[])
    def test_quota_sign_does_not_stop_healthy_seat(self):
        def fake(req,actor,history):
            if actor=='GPT':raise runner.GateError('HTTP 429 from provider (provider_rate_limit)')
            return {'actor':actor,'answer':'verified','reference':{}}
        x=self.req();x['actors']=['GPT','GEMINI'];x['cycles']=2
        with patch.object(runner,'cycle',side_effect=fake),patch.object(runner,'publish'):
            result=runner.run(x)
        self.assertEqual(result['actors']['GPT']['display_status'],'Out to lunch')
        self.assertEqual(result['actors']['GPT']['pause_reason'],'usage_limit')
        self.assertEqual(result['actors']['GEMINI']['cycles'],2)
        self.assertEqual(result['status'],'PARTIAL')
        self.assertFalse(runner.usage_limited(runner.GateError('CLAUDE client failed; check local sign-in and plan limits')))
    def test_drift_restarts_once_with_shared_budget(self):
        calls=[]
        def fake(req,actor,history):
            calls.append(req['_call_budget']);req['_call_budget']['used']+=1
            if len(calls)==1:raise runner.ReReferenceRequired('drift','head changed')
            self.assertIn('head changed',req['question'])
            return {'actor':actor,'answer':'fresh','reference':{}}
        with patch.object(runner,'cycle',side_effect=fake),patch.object(runner,'publish'):
            result=runner.run(self.req())
        self.assertEqual(result['status'],'COMPLETE')
        self.assertIs(calls[0],calls[1]);self.assertEqual(calls[0]['used'],2)
        self.assertEqual(result['turns'][0]['rereference_events'][0]['reason'],'drift')
    def test_persistent_confusion_stops_after_one_restart(self):
        with patch.object(runner,'cycle',side_effect=runner.ReReferenceRequired('confusion','unresolved')) as cycle,patch.object(runner,'publish'):
            result=runner.run(self.req())
        self.assertEqual(cycle.call_count,2)
        self.assertEqual(result['actors']['GEMINI']['pause_reason'],'rereference_required')
        self.assertEqual(result['turns'],[])
    def test_model_reference_issue_interrupts_before_synthesis(self):
        for reason in ['drift','assumption','confusion']:
            with self.subTest(reason=reason),patch.object(runner,'scan',side_effect=self.source),patch.object(runner,'invoke',return_value={'answer':json.dumps({'reference_issue':{'reason':reason,'detail':'uncertain repo fact'}})}) as model:
                with self.assertRaises(runner.ReReferenceRequired) as caught:runner.cycle(self.req(),'GPT',[])
                self.assertEqual(caught.exception.reason,reason);self.assertEqual(model.call_count,1)
    def test_explicit_rereference_tool_interrupts(self):
        def ask(*args):return {'answer':json.dumps({'lens_tool':{'name':'rereference','arguments':{'reason':'assumption','detail':'need current source'}}})}
        with self.assertRaises(runner.ReReferenceRequired) as caught:runner.lens_exchange('GPT','q',ask,[],[])
        self.assertEqual(caught.exception.reason,'assumption')
    def test_gemini_does_not_retry_another_model_after_quota(self):
        with patch.dict(runner.os.environ,{'GEMINI_API_KEY':'test','GEMINI_MODEL':'test'}),patch.object(runner,'request_json',side_effect=runner.GateError('HTTP 429 from google')) as request:
            with self.assertRaises(runner.UsageLimit):runner.gemini('s','p')
        self.assertEqual(request.call_count,1)
    def test_unknown_tool_is_not_executed(self):
        with self.assertRaisesRegex(runner.GateError,'Unregistered'):runner.lens_request(json.dumps({'lens_tool':{'name':'shell','arguments':{'cmd':'rm'}}}))
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
