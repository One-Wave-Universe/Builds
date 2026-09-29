#!/usr/bin/env python3
import json, os, sys, time, random, urllib.request, urllib.error
from pathlib import Path
BASE="https://generativelanguage.googleapis.com/v1beta"

def call(url,key,body=None):
    h={"x-goog-api-key":key,"Content-Type":"application/json"}
    r=urllib.request.Request(url,data=None if body is None else json.dumps(body).encode(),headers=h,method="GET" if body is None else "POST")
    with urllib.request.urlopen(r,timeout=90) as x:return json.load(x)

def models(key):
    x=call(BASE+"/models?pageSize=1000",key)
    ms=[m["name"] for m in x.get("models",[]) if "generateContent" in m.get("supportedGenerationMethods",[])]
    def rank(n):
        s=n.lower()
        return (0 if "flash-lite" in s else 1 if "flash" in s else 2 if "pro" in s else 3, n)
    return sorted(ms,key=rank)

def generate(key,model,prompt):
    body={"contents":[{"role":"user","parts":[{"text":prompt}]}],"generationConfig":{"temperature":0.2,"maxOutputTokens":1200}}
    return call(BASE+"/"+model+":generateContent",key,body)

def gemini(question,previous="",evidence=None):
    key=os.environ["GEMINI_API_KEY"]
    lens_path=Path("two-ai-dialogue/ONE_WAVE_LENS.md")
    lens_text=lens_path.read_text() if lens_path.exists() else ""
    evidence_text = "(none supplied)"
    if evidence:
        evidence_text=json.dumps(evidence,ensure_ascii=False)
    prompt=("MANDATORY ONE-WAVE INTERPRETATION LENS (method/ontology contract, NOT proof):\n"+lens_text+"\n\nOriginal question:\n"+question+"\n\nPrevious visible answer:\n"+(previous or "(none)")+
      "\n\nREPOSITORY EVIDENCE PACK (these and only these repository files count as actually read):\n"+evidence_text+
      "\n\nGive the next concise answer. Correct omissions/errors and move toward a finished answer. "
      "Do not expose hidden chain-of-thought. Give conclusions, objections, evidence needs, and unresolved items.")
    errors=[]
    for model in models(key)[:12]:
        for attempt in range(4):
            try:
                x=generate(key,model,prompt)
                parts=x.get("candidates",[{}])[0].get("content",{}).get("parts",[])
                answer="".join(p.get("text","") for p in parts).strip()
                if answer:
                    return {"actor":"GEMINI","answer":answer,"provider":"google","model":model.split("/",1)[-1],
                            "response_id":x.get("responseId"),"attempt":attempt+1,"fallback_errors":errors}
                errors.append({"model":model,"attempt":attempt+1,"error":"empty response"})
                break
            except urllib.error.HTTPError as e:
                code=e.code
                errors.append({"model":model,"attempt":attempt+1,"http":code})
                if code in (408,429) or 500 <= code < 600:
                    time.sleep(min(8,2**attempt)+random.random())
                    continue
                break
            except Exception as e:
                errors.append({"model":model,"attempt":attempt+1,"error":type(e).__name__})
                time.sleep(min(8,2**attempt)+random.random())
    raise RuntimeError("Gemini models exhausted: "+json.dumps(errors))

if __name__=="__main__":
    x=json.loads(Path(sys.argv[1]).read_text())
    try:
        evidence=None
        ep=x.get("evidence_pack")
        if ep:
            evidence=json.loads(Path(ep).read_text())
        turn=gemini(x["question"],x.get("previous_visible_answer",""),evidence)
        out={"schema":"one-wave-gemini-receipt/v1","request_id":x["id"],"status":"COMPLETE","turn":turn}
    except Exception as e:
        out={"schema":"one-wave-gemini-receipt/v1","request_id":x["id"],"status":"HOLD","error":str(e)}
    print(json.dumps(out))
    sys.exit(0 if out["status"]=="COMPLETE" else 2)
