#!/usr/bin/env python3
"""One-Wave Brain Buddy command program.

This is the stable program entrypoint for repo-grounded Gemini work.
It does not contain provider secrets and does not depend on Desktop Commander,
Jetson, browser extensions, or local Gemini OAuth.

Modes:
  request  - emit a validated one-shot Gemini request JSON
  dialogue - emit a validated ChatGPT<->Gemini dialogue request JSON
  verify   - verify a returned receipt matches the request id
"""
import argparse, json, pathlib, sys

SCIENCE_REPO="One-Wave-Universe/One-Wave-Science"

def base_request(a, dialogue=False):
    q=a.question.strip()
    if not q: raise ValueError("question required")
    rid=a.id.strip()
    if not rid: raise ValueError("id required")
    x={
      "id":rid,
      "question":q,
      "repo_read":{
        "repository":SCIENCE_REPO,
        "root":"peer-repo",
        "query":a.query.strip() or q,
      },
      "source_class":"real",
      "execution_class":"reference-only",
    }
    if dialogue:
        x["actors"]=["CHATGPT","GEMINI"]
        x["max_turns"]=a.max_turns
    else:
        x["peer"]="gemini"
    return x

def verify(req_path, receipt_path):
    req=json.loads(pathlib.Path(req_path).read_text())
    rec=json.loads(pathlib.Path(receipt_path).read_text())
    rid=req["id"]
    got=rec.get("request_id",rec.get("id"))
    if got!=rid: raise ValueError(f"request id mismatch: {rid} != {got}")
    status=rec.get("status")
    if status not in {"COMPLETE","AGREED_RESOLUTION","AGREED_NEXT_ACTION","MAX_TURNS","HOLD"}:
        raise ValueError(f"unexpected status: {status}")
    return {"ok":True,"id":rid,"status":status}

def main():
    ap=argparse.ArgumentParser(prog="brain-buddy")
    sp=ap.add_subparsers(dest="cmd",required=True)
    for name in ("request","dialogue"):
        p=sp.add_parser(name)
        p.add_argument("--id",required=True)
        p.add_argument("--question",required=True)
        p.add_argument("--query",default="")
        if name=="dialogue": p.add_argument("--max-turns",type=int,default=4,choices=range(2,9))
        p.add_argument("--output")
    v=sp.add_parser("verify");v.add_argument("request");v.add_argument("receipt")
    a=ap.parse_args()
    if a.cmd=="verify":
        print(json.dumps(verify(a.request,a.receipt),indent=2)); return
    x=base_request(a,a.cmd=="dialogue")
    raw=json.dumps(x,indent=2)+"\n"
    if a.output: pathlib.Path(a.output).write_text(raw)
    else: sys.stdout.write(raw)

if __name__=="__main__":
    main()
