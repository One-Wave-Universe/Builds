#!/usr/bin/env python3
import json, os, sys, time, urllib.request, urllib.error
from pathlib import Path
BASE="https://api.x.ai/v1"

def generate(key,model,prompt):
    body={"model":model,"messages":[{"role":"user","content":prompt}],"temperature":0.2}
    req=urllib.request.Request(BASE+"/chat/completions",data=json.dumps(body).encode(),
        headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=90) as r:return json.load(r)

def grok(question,previous="",evidence=None):
    key=os.environ["XAI_API_KEY"]
    lens=Path("two-ai-dialogue/ONE_WAVE_LENS.md").read_text()
    ev=json.dumps(evidence,ensure_ascii=False) if evidence else "(none supplied)"
    prompt=("MANDATORY ONE-WAVE INTERPRETATION LENS (method/ontology contract, NOT proof):\n"+lens+
      "\n\nOriginal question:\n"+question+"\n\nPrevious visible answer:\n"+(previous or "(none)")+
      "\n\nREPOSITORY EVIDENCE PACK (these and only these repository files count as actually read):\n"+ev+
      "\n\nGive a concise critical answer. Do not expose hidden chain-of-thought. Give conclusions, objections, evidence needs, falsification conditions and unresolved items.")
    models=[os.getenv("XAI_MODEL","grok-4-fast-reasoning"),"grok-4-fast-non-reasoning","grok-3-mini"]
    errors=[]
    for model in dict.fromkeys(models):
      for attempt in range(3):
        try:
          x=generate(key,model,prompt)
          ans=x["choices"][0]["message"]["content"].strip()
          if ans:return {"actor":"GROK","answer":ans,"provider":"xai","model":model,"response_id":x.get("id"),"attempt":attempt+1,"fallback_errors":errors}
        except urllib.error.HTTPError as e:
          body=e.read().decode(errors="replace")[:500]
          errors.append({"model":model,"attempt":attempt+1,"http":e.code,"error":body})
          if e.code in (408,429) or 500<=e.code<600: time.sleep(min(6,2**attempt)); continue
          break
        except Exception as e:
          errors.append({"model":model,"attempt":attempt+1,"error":type(e).__name__})
          break
    raise RuntimeError("Grok models exhausted: "+json.dumps(errors))

if __name__=="__main__":
    x=json.loads(Path(sys.argv[1]).read_text())
    try:
      evidence=json.loads(Path(x["evidence_pack"]).read_text()) if x.get("evidence_pack") else None
      turn=grok(x["question"],x.get("previous_visible_answer",""),evidence)
      out={"schema":"one-wave-grok-receipt/v1","request_id":x["id"],"status":"COMPLETE","turn":turn}
    except Exception as e:
      out={"schema":"one-wave-grok-receipt/v1","request_id":x["id"],"status":"HOLD","error":str(e)}
    print(json.dumps(out))
    sys.exit(0 if out["status"]=="COMPLETE" else 2)
