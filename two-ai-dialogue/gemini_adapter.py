#!/usr/bin/env python3
import json, os, sys, urllib.request
from pathlib import Path

def gemini(question, previous=""):
    key=os.environ["GEMINI_API_KEY"]
    prompt=("Original question:\n"+question+"\n\nPrevious visible answer:\n"+(previous or "(none)")+
           "\n\nReturn a concise next answer that corrects omissions/errors and moves toward a finished answer. "
           "Do not provide hidden chain-of-thought; provide conclusions, objections, evidence needs, and unresolved items.")
    body={"contents":[{"parts":[{"text":prompt}]}]}
    url="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key="+key
    req=urllib.request.Request(url,data=json.dumps(body).encode(),headers={"Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(req,timeout=60) as r:
        out=json.load(r)
    answer="".join(p.get("text","") for p in out["candidates"][0]["content"]["parts"])
    return {"actor":"GEMINI","answer":answer,"provider":"google","model":"gemini-2.5-flash"}

if __name__=="__main__":
    x=json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps({"schema":"one-wave-gemini-receipt/v1","request_id":x["id"],"turn":gemini(x["question"])}))
