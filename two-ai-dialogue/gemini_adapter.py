#!/usr/bin/env python3
import json, os, sys, urllib.request
from pathlib import Path

BASE="https://generativelanguage.googleapis.com/v1beta"
def request(url, key, body=None):
    headers={"x-goog-api-key":key,"Content-Type":"application/json"}
    data=None if body is None else json.dumps(body).encode()
    req=urllib.request.Request(url,data=data,headers=headers,method="GET" if body is None else "POST")
    with urllib.request.urlopen(req,timeout=60) as r:return json.load(r)

def choose_model(key):
    x=request(BASE+"/models",key)
    ms=[m for m in x.get("models",[]) if "generateContent" in m.get("supportedGenerationMethods",[])]
    preferred=["gemini-3.8-flash","gemini-3.7-flash","gemini-3.6-flash","gemini-3.5-flash","gemini-3.1-flash-lite","gemini-2.0-flash"]
    names={m["name"].split("/",1)[-1] for m in ms}
    for p in preferred:
        if p in names:return p
    if not ms:raise RuntimeError("No generateContent model available to this key")
    return ms[0]["name"].split("/",1)[-1]

def gemini(question, previous=""):
    key=os.environ["GEMINI_API_KEY"]; model=choose_model(key)
    prompt=("Original question:\n"+question+"\n\nPrevious visible answer:\n"+(previous or "(none)")+
      "\n\nGive the next concise answer. Correct omissions/errors and move toward a finished answer. "
      "Do not expose hidden chain-of-thought. Give conclusions, objections, evidence needs, and unresolved items.")
    x=request(BASE+"/models/"+model+":generateContent",key,{"contents":[{"parts":[{"text":prompt}]}]})
    answer="".join(p.get("text","") for p in x["candidates"][0]["content"]["parts"])
    return {"actor":"GEMINI","answer":answer,"provider":"google","model":model}

if __name__=="__main__":
    x=json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps({"schema":"one-wave-gemini-receipt/v1","request_id":x["id"],"turn":gemini(x["question"])}))
