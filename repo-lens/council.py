"""Answer first, then independent council review. No timed or endless cycles."""
import concurrent.futures,json,threading

def vote(answer):
    text=answer.strip()
    if text.startswith('```') and text.endswith('```'):text=text.split('\n',1)[1].rsplit('```',1)[0]
    try:value=json.loads(text)
    except ValueError:return {'decision':'abstain','answer':answer,'reason':'No explicit review decision'}
    if not isinstance(value,dict) or value.get('decision') not in {'agree','revise','abstain'} or not isinstance(value.get('answer'),str):
        return {'decision':'abstain','answer':answer,'reason':'Invalid review decision'}
    return value

def conduct(req,complete,emit,is_usage_limit):
    actors=req['actors'];lead=req.get('lead_actor',actors[0]);lock=threading.RLock()
    budgets={actor:{'used':0} for actor in actors}
    result={'schema':'repo-lens/v2','workflow':'answer_then_council','id':req['id'],'repository':req['repository'],'question':req['question'],'lead_actor':lead,'status':'RUNNING','phase':'ANSWERING','actors':{a:{'status':'QUEUED','cycles':0,'activity':'Answering' if a==lead else 'Waiting for lead answer'} for a in actors},'turns':[]}
    def publish():emit(result)
    def history():
        with lock:return [{k:v for k,v in t.items() if k not in {'reference','segment_calls','metadata_sources'}} for t in result['turns']]
    def progress(actor,data):
        with lock:result['actors'][actor].update(data);publish()
    history.progress=progress
    def perform(actor,question,role,round_number):
        with lock:result['actors'][actor].update({'status':'REFERENCING','activity':role});publish()
        try:
            turn=complete({**req,'question':question,'_call_budget':budgets[actor]},actor,history)
            turn.update({'actor':actor,'cycle':round_number,'role':role,'status':'COMPLETE'})
            if role=='Council review':
                decision=vote(turn['answer']);turn['review_decision']=decision['decision'];turn['answer']=decision['answer']
            with lock:
                result['turns'].append(turn);result['actors'][actor].update({'status':'COMPLETE','display_status':'COMPLETE','cycles':round_number,'activity':'Finished'});publish()
            return turn
        except Exception as error:
            with lock:
                result['actors'][actor].update({'status':'HOLD','display_status':'Out to lunch' if is_usage_limit(error) else 'HOLD','pause_reason':'usage_limit' if is_usage_limit(error) else 'error','error':str(error),'activity':'Parked'});publish()
            return None
    publish()
    answer=perform(lead,req['question']+'\nYou are the lead AI. Answer to the best of your ability from the repository. Use metadata tools when necessary. Then your answer will be handed to the council. Cite inspected paths.','Lead answer',1)
    if answer is None:
        for actor in actors:
            if actor!=lead:result['actors'][actor].update({'status':'SKIPPED','activity':'No completed lead answer to review'})
        result.update({'status':'HOLD','phase':'FINISHED','consensus':{'status':'BLOCKED','reason':'Lead produced no complete referenced answer'}});publish();return result
    reviewers=[a for a in actors if a!=lead]
    decisions={};review_turns={}
    for round_number in range(1,3):
        result['phase']='COUNCIL_REVIEW';publish()
        question=req['question']+'\nReview the lead answer below using fresh repository references and metadata when necessary. Address evidence, errors, uncertainty and disagreements. Return ONLY JSON with decision (agree, revise, or abstain) and answer (your concise source-cited review). Agreement is not scientific proof.\nLEAD ANSWER:\n'+answer['answer']
        eligible=[a for a in reviewers if result['actors'][a]['status']!='HOLD']
        with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,len(eligible))) as pool:
            reviewed=list(pool.map(lambda actor:perform(actor,question,'Council review',round_number),eligible))
        decisions.update({turn['actor']:turn['review_decision'] for turn in reviewed if turn})
        review_turns.update({turn['actor']:turn for turn in reviewed if turn})
        lead_commits=answer.get('reference',{}).get('repository_commits',{})
        drift=[a for a,t in review_turns.items() if t.get('reference',{}).get('repository_commits',{})!=lead_commits]
        if round_number==2 or (not drift and not any(d=='revise' for d in decisions.values())):break
        result['phase']='LEAD_REVISION';publish()
        answer=perform(lead,req['question']+'\nThe council identified corrections. Revise your answer against fresh source and the actual reviews below. Resolve what evidence supports and state remaining gaps. Do not invent agreement.\n'+json.dumps(history()),'Lead revision',2)
        if answer is None:break
    missing=[a for a in reviewers if a not in decisions or result['actors'][a]['status']=='HOLD']
    lead_commits=(answer or {}).get('reference',{}).get('repository_commits',{})
    drift=[a for a,t in review_turns.items() if t.get('reference',{}).get('repository_commits',{})!=lead_commits]
    agreed=answer is not None and bool(lead_commits) and bool(reviewers) and not missing and not drift and all(decisions.get(a)=='agree' for a in reviewers)
    result.update({'status':'COMPLETE' if not missing and answer is not None else 'PARTIAL','phase':'FINISHED','checked_answer':answer['answer'] if answer else None,'consensus':{'status':'AGREED' if agreed else 'BLOCKED' if missing or answer is None else 'UNRESOLVED','decisions':decisions,'missing_votes':missing,'reference_drift':drift,'scope':'Agreement of all requested council reviewers on this answer and the same verified repository commits; not scientific proof','repository_updates':'No code update without a separate exact proposal, current-base review and verification'}})
    publish();return result
