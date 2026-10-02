#!/usr/bin/env python3
"""One-Wave Brain Buddy portable request/receipt contract.

The core is UI-neutral so the same JSON contract can back Linux and Android.
"""
import argparse,json,pathlib,sys
SCIENCE_REPO="One-Wave-Universe/One-Wave-Science"
DEFAULT_ACTORS=["CHATGPT","GEMINI","DEEPSEEK"]

def base_request(a,dialogue=False):
    q=a.question.strip();rid=a.id.strip()
    if not q:raise ValueError("question required")
    if not rid:raise ValueError("id required")
    x={"id":rid,"question":q,"repo_read":{"repository":SCIENCE_REPO,"root":"peer-repo","query":a.query.strip() or q},
       "source_class":"real","execution_class":"reference-only"}
    if dialogue:x["actors"]=DEFAULT_ACTORS[:];x["max_turns"]=a.max_turns
    else:x["peer"]="gemini"
    return x

def verify(req_path,receipt_path):
    req=json.loads(pathlib.Path(req_path).read_text());rec=json.loads(pathlib.Path(receipt_path).read_text())
    rid=req["id"];got=rec.get("request_id",rec.get("id"))
    if got!=rid:raise ValueError(f"request id mismatch: {rid} != {got}")
    status=rec.get("status")
    if status not in {"COMPLETE","AGREED_RESOLUTION","AGREED_NEXT_ACTION","MAX_TURNS","HOLD"}:raise ValueError(f"unexpected status: {status}")
    return {"ok":True,"id":rid,"status":status}

def main():
    ap=argparse.ArgumentParser(prog="brain-buddy");sp=ap.add_subparsers(dest="cmd",required=True)
    for name in ("request","dialogue"):
        p=sp.add_parser(name);p.add_argument("--id",required=True);p.add_argument("--question",required=True);p.add_argument("--query",default="")
        if name=="dialogue":p.add_argument("--max-turns",type=int,default=6,choices=range(2,13))
        p.add_argument("--output")
    v=sp.add_parser("verify");v.add_argument("request");v.add_argument("receipt");a=ap.parse_args()
    if a.cmd=="verify":print(json.dumps(verify(a.request,a.receipt),indent=2));return
    raw=json.dumps(base_request(a,a.cmd=="dialogue"),indent=2)+"\n"
    pathlib.Path(a.output).write_text(raw) if a.output else sys.stdout.write(raw)
if __name__=="__main__":main()
