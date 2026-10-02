#!/usr/bin/env python3
"""DeepSeek adapter for the portable Brain Buddy visible-turn contract."""
import json,os,sys,urllib.request,urllib.error
from pathlib import Path
URL=os.environ.get("DEEPSEEK_BASE_URL","https://api.deepseek.com/chat/completions")
MODEL=os.environ.get("DEEPSEEK_MODEL","deepseek-chat")

def run(x):
    key=os.environ["DEEPSEEK_API_KEY"]
    evidence=json.loads(Path(x["evidence_pack"]).read_text()) if x.get("evidence_pack") else None
    prompt=("Use only the shared repository/data evidence below as the common factual reference. "
      "Critique the other visible participants, correct errors, state what is supported versus unproven, "
      "and move toward a common conclusion and next falsifiable test. Do not expose hidden chain-of-thought.\n\n"
      "QUESTION:\n"+x["question"]+"\n\nVISIBLE HISTORY:\n"+json.dumps(x.get("visible_history",[]),ensure_ascii=False)+
      "\n\nSHARED EVIDENCE PACK:\n"+json.dumps(evidence,ensure_ascii=False))
    body={"model":MODEL,"messages":[{"role":"user","content":prompt}],"temperature":0.2,"max_tokens":1200}
    req=urllib.request.Request(URL,data=json.dumps(body).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=120) as r:out=json.load(r)
    answer=out["choices"][0]["message"]["content"].strip()
    return {"actor":"DEEPSEEK","answer":answer,"provider":"deepseek","model":out.get("model",MODEL),"response_id":out.get("id")}

if __name__=="__main__":
    x=json.loads(Path(sys.argv[1]).read_text())
    try:out={"schema":"one-wave-deepseek-receipt/v1","request_id":x["id"],"status":"COMPLETE","turn":run(x)}
    except Exception as e:out={"schema":"one-wave-deepseek-receipt/v1","request_id":x["id"],"status":"HOLD","error":str(e)}
    print(json.dumps(out));sys.exit(0 if out["status"]=="COMPLETE" else 2)
