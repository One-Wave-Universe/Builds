#!/usr/bin/env python3
import argparse,json,pathlib,sys
STATES={"IDLE","PRIMED","EXECUTING","VECTORING","RESOLVING","DONE","BLOCKED"}

def load(p): return json.loads(pathlib.Path(p).read_text())

def validate(r):
    errs=[]; lanes={x["id"] for x in r.get("lanes",[])}; ids=set()
    for j in r.get("jobs",[]):
        jid=j.get("id","?")
        if jid in ids: errs.append(f"{jid}: duplicate id")
        ids.add(jid)
        if j.get("lane") not in lanes: errs.append(f"{jid}: unknown lane")
        if j.get("state") not in STATES: errs.append(f"{jid}: invalid state")
        if not j.get("acceptance"): errs.append(f"{jid}: missing acceptance")
        if j.get("state")=="DONE" and not j.get("receipts"): errs.append(f"{jid}: DONE without receipt")
        if j.get("state")=="BLOCKED" and not j.get("blockers"): errs.append(f"{jid}: BLOCKED without blocker")
    for j in r.get("jobs",[]):
        for d in j.get("depends",[]):
            if d not in ids: errs.append(f'{j["id"]}: missing dependency {d}')
    return errs

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest="cmd",required=True)
    for c in ("validate","summary"): q=sp.add_parser(c); q.add_argument("registry")
    a=ap.parse_args(); r=load(a.registry); e=validate(r)
    if a.cmd=="validate":
        print(json.dumps({"ok":not e,"errors":e},indent=2)); raise SystemExit(0 if not e else 2)
    by={}
    for j in r["jobs"]: by.setdefault(j["lane"],[]).append(j)
    for l in r["lanes"]:
        js=by.get(l["id"],[]); print(f'[{l["name"]}]')
        for j in js: print(f'  {j["state"]:10} {j["id"]}: {j["title"]}')
    if e: print("\nVALIDATION ERRORS:\n- "+"\n- ".join(e))
if __name__=="__main__": main()
