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
        return (0 if "flash-lite" in s else 1 if "flash" in s else 2 if "pro" in s else 3,n)
    return sorted(ms,key=rank)

def generate(key,model,prompt,research=True):
    body={"contents":[{"role":"user","parts":[{"text":prompt}]}],
          "generationConfig":{"temperature":0.2,"maxOutputTokens":1400}}
    if research:
        body["tools"]=[{"google_search":{}}]
    return call(BASE+"/"+model+":generateContent",key,body)

def source_list(raw):
    out=[];seen=set()
    for cand in raw.get("candidates",[]):
        gm=cand.get("groundingMetadata") or {}
        for chunk in gm.get("groundingChunks",[]) or []:
            web=chunk.get("web") or {}
            uri=web.get("uri")
            if uri and uri not in seen:
                seen.add(uri)
                out.append({"title":web.get("title"),"uri":uri})
    return out

def gemini(question,previous="",evidence=None,research=True):
    key=os.environ["GEMINI_API_KEY"]
    lens_path=Path("two-ai-dialogue/ONE_WAVE_LENS.md")
    lens_text=lens_path.read_text() if lens_path.exists() else ""
    evidence_text=json.dumps(evidence,ensure_ascii=False) if evidence else "(none supplied)"
    prompt=("MANDATORY ORDER:\n"
            "1. Read the supplied One-Wave repository evidence first and treat it as project reference, not proof.\n"
            "2. From that repo evidence, state the exact claim/test being evaluated before using outside evidence.\n"
            "3. Consult metadata next. Metadata is provenance/availability evidence, not proof.\n"
            "4. Only then consult CERN Open Data, GWOSC/LIGO, spectroscopy, or other external wave-domain data/research when enabled.\n"
            "5. Keep external provider material separate from One-Wave interpretations.\n"
            "6. Answer the original question and identify exact repo paths plus important metadata and external sources used.\n\n"
            "ONE-WAVE INTERPRETATION LENS:\n"+lens_text+
            "\n\nOriginal question:\n"+question+
            "\n\nPrevious visible answer:\n"+(previous or "(none)")+
            "\n\nREPOSITORY EVIDENCE PACK:\n"+evidence_text+
            "\n\nDo not expose hidden chain-of-thought. Give conclusions, objections, evidence needs, and unresolved items.")
    errors=[]
    for model in models(key)[:12]:
        for attempt in range(4):
            try:
                raw=generate(key,model,prompt,research)
                parts=raw.get("candidates",[{}])[0].get("content",{}).get("parts",[])
                answer="".join(p.get("text","") for p in parts).strip()
                if answer:
                    return {"actor":"GEMINI","answer":answer,"provider":"google",
                            "model":model.split("/",1)[-1],"response_id":raw.get("responseId"),
                            "attempt":attempt+1,"fallback_errors":errors,
                            "research_enabled":bool(research),"research_sources":source_list(raw)}
                errors.append({"model":model,"attempt":attempt+1,"error":"empty response"})
                break
            except urllib.error.HTTPError as e:
                code=e.code
                errors.append({"model":model,"attempt":attempt+1,"http":code})
                if code in (408,429) or 500<=code<600:
                    time.sleep(min(8,2**attempt)+random.random());continue
                break
            except Exception as e:
                errors.append({"model":model,"attempt":attempt+1,"error":type(e).__name__})
                time.sleep(min(8,2**attempt)+random.random())
    raise RuntimeError("Gemini models exhausted: "+json.dumps(errors))

if __name__=="__main__":
    x=json.loads(Path(sys.argv[1]).read_text())
    try:
        evidence=None
        if x.get("evidence_pack"):
            evidence=json.loads(Path(x["evidence_pack"]).read_text())
        turn=gemini(x["question"],x.get("previous_visible_answer",""),evidence,bool(x.get("research",True)))
        out={"schema":"one-wave-gemini-receipt/v1","request_id":x["id"],"status":"COMPLETE","turn":turn}
    except Exception as e:
        out={"schema":"one-wave-gemini-receipt/v1","request_id":x["id"],"status":"HOLD","error":str(e)}
    print(json.dumps(out))
    sys.exit(0 if out["status"]=="COMPLETE" else 2)
