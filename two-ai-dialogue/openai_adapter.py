#!/usr/bin/env python3
import json, os, sys, time, urllib.request, urllib.error
API="https://api.openai.com/v1/responses"
MODELS=["gpt-5.6-luna","gpt-5.6-terra","gpt-5.6-sol"]

def text_from(x):
    if x.get("output_text"): return x["output_text"]
    out=[]
    for item in x.get("output",[]):
        for p in item.get("content",[]):
            if p.get("type")=="output_text": out.append(p.get("text",""))
    return "".join(out).strip()

def run(question, previous="", settled=None, unresolved=None):
    key=os.environ["OPENAI_API_KEY"]
    prompt=("Original question:\n"+question+"\n\nPrevious opposing AI answer:\n"+(previous or "(none)")+
      "\n\nSettled points:\n"+json.dumps(settled or [])+"\nUnresolved:\n"+json.dumps(unresolved or [])+
      "\n\nRespond as an engineering peer reviewer. Do not expose hidden chain-of-thought. "
      "State conclusions, objections, unresolved evidence, and a concrete proposed resolution OR proposed next action.")
    errors=[]
    for model in MODELS:
      for attempt in range(3):
        try:
          body={"model":model,"input":prompt,"max_output_tokens":1400}
          req=urllib.request.Request(API,data=json.dumps(body).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
          with urllib.request.urlopen(req,timeout=120) as r:x=json.load(r)
          ans=text_from(x)
          if ans:return {"actor":"CHATGPT","answer":ans,"provider":"openai","model":model,"response_id":x.get("id"),"attempt":attempt+1,"fallback_errors":errors}
          errors.append({"model":model,"attempt":attempt+1,"error":"empty"})
          break
        except urllib.error.HTTPError as e:
          errors.append({"model":model,"attempt":attempt+1,"http":e.code})
          if e.code in (408,409,429) or 500<=e.code<600: time.sleep(min(8,2**attempt)); continue
          break
    raise RuntimeError("OpenAI models exhausted: "+json.dumps(errors))

if __name__=="__main__":
    x=json.loads(open(sys.argv[1]).read())
    try:
      t=run(x["question"])
      o={"schema":"one-wave-openai-receipt/v1","request_id":x["id"],"status":"COMPLETE","turn":t}
    except Exception as e:o={"schema":"one-wave-openai-receipt/v1","request_id":x["id"],"status":"HOLD","error":str(e)}
    print(json.dumps(o)); sys.exit(0 if o["status"]=="COMPLETE" else 2)
