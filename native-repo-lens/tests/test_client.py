import sys,unittest,json,urllib.parse
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).parents[1]/'linux'))
import lens

class Contracts(unittest.TestCase):
    def test_question_is_not_a_shell_command(self):
        question='Read `$(touch /tmp/no)` and explain A+\nB−.'
        with patch.object(lens,'reference',return_value={'repository':'One-Wave-Universe/Builds','branch':'main','commit':'a'*40}):
            x=lens.prepare('Builds',question,['GPT'],1,True)
        q=urllib.parse.parse_qs(urllib.parse.urlsplit(x['submission_url']).query)
        self.assertEqual(json.loads(q['value'][0])['question'],question)
        self.assertEqual(len(x['packet']['metadata_queries']),2)
    def test_invalid_input_does_not_request_reference(self):
        with patch.object(lens,'reference') as r:
            for args in [('Other','q',['GPT'],1,True),('Builds','q',['CLAUDE','CLAUDE'],1,True),('Builds','q',['GPT'],0,True)]:
                with self.assertRaises(ValueError):lens.prepare(*args)
            r.assert_not_called()
    def test_wrong_receipt_is_rejected(self):
        with patch.object(lens,'get',return_value=json.dumps({'id':'other','schema':'repo-lens/v1'})):
            with self.assertRaisesRegex(ValueError,'identity'):lens.result('request')
    def test_submodule_or_truncated_tree_holds(self):
        for tree in [{'truncated':True},{'tree':[{'type':'commit','path':'sub'}]}]:
            with patch.object(lens,'api',side_effect=[{'default_branch':'main'},{'sha':'a'*40,'commit':{'tree':{'sha':'b'*40}}},tree]):
                with self.assertRaises(ValueError):lens.reference('Builds')
    def test_failed_actor_does_not_hide_completed_peer(self):
        x={'id':'x','status':'PARTIAL','actors':{'CLAUDE':{'status':'HOLD','cycles':0,'error':'Sign-in required'},'GPT':{'status':'COMPLETE','cycles':1}},'turns':[{'actor':'GPT','cycle':1,'status':'COMPLETE','answer':'actual answer','reference':{'file_count':197},'segments_read':5}]}
        text=lens.display(x);self.assertIn('Sign-in required',text);self.assertIn('actual answer',text)

if __name__=='__main__':unittest.main()
