import unittest,json,copy
from council import conduct
from runner import GateError,usage_limited

class Council(unittest.TestCase):
    def req(self):return {'id':'test','repository':'One-Wave-Universe/Builds','question':'What is built?','actors':['GPT','GEMINI','DEEPSEEK'],'lead_actor':'GPT'}
    def test_lead_finishes_before_review_and_all_votes_are_needed(self):
        calls=[];receipts=[]
        def complete(req,actor,history):
            calls.append(actor)
            if actor!='GPT':self.assertEqual(history()[0]['actor'],'GPT')
            return {'answer':'source.py built' if actor=='GPT' else json.dumps({'decision':'agree','answer':'source.py supported'}),'reference':{'repository_commits':{'repo':'sha'}}}
        result=conduct(self.req(),complete,lambda r:receipts.append(copy.deepcopy(r)),usage_limited)
        self.assertEqual(calls[0],'GPT');self.assertEqual(result['consensus']['status'],'AGREED')
        self.assertEqual(len(result['turns']),3)
    def test_limit_is_missing_vote_and_does_not_stop_healthy_review(self):
        def complete(req,actor,history):
            if actor=='GEMINI':raise GateError('HTTP 429 from provider')
            return {'answer':'source.py built' if actor=='GPT' else json.dumps({'decision':'agree','answer':'source.py supported'})}
        result=conduct(self.req(),complete,lambda r:None,usage_limited)
        self.assertEqual(result['actors']['GEMINI']['display_status'],'Out to lunch')
        self.assertEqual(result['actors']['DEEPSEEK']['status'],'COMPLETE')
        self.assertEqual(result['consensus']['status'],'BLOCKED');self.assertEqual(result['consensus']['missing_votes'],['GEMINI'])
    def test_disagreement_allows_one_revision_without_endless_rounds(self):
        calls=[];budgets={}
        def complete(req,actor,history):
            calls.append(actor)
            if actor in budgets:self.assertIs(budgets[actor],req['_call_budget'])
            budgets[actor]=req['_call_budget']
            return {'answer':'source.py revised' if actor=='GPT' else json.dumps({'decision':'revise','answer':'source.py still unproven'})}
        result=conduct(self.req(),complete,lambda r:None,usage_limited)
        self.assertEqual(calls.count('GPT'),2);self.assertEqual(calls.count('GEMINI'),2)
        self.assertEqual(result['consensus']['status'],'UNRESOLVED')
    def test_plain_answer_is_not_invented_agreement(self):
        result=conduct(self.req(),lambda *args:{'answer':'sounds good source.py'},lambda r:None,usage_limited)
        self.assertEqual(result['consensus']['status'],'UNRESOLVED')
    def test_lead_failure_prevents_reviews_of_nonexistent_answer(self):
        calls=[]
        def complete(req,actor,history):calls.append(actor);raise GateError('bridge unavailable')
        result=conduct(self.req(),complete,lambda r:None,usage_limited)
        self.assertEqual(calls,['GPT']);self.assertEqual(result['status'],'HOLD')
    def test_a_single_seat_is_not_council_consensus(self):
        req=self.req();req['actors']=['GPT']
        result=conduct(req,lambda *args:{'answer':'source.py built'},lambda r:None,usage_limited)
        self.assertEqual(result['consensus']['status'],'UNRESOLVED')

if __name__=='__main__':unittest.main()
