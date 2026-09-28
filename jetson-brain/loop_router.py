#!/usr/bin/env python3
import argparse,json,hashlib,time

def digest(x): return hashlib.sha256(json.dumps(x,sort_keys=True).encode()).hexdigest()[:16]

class FieldCPU:
    name="field-cpu-reference"
    def run(self, state):
        x=state["value"]
        return {"candidate":x+1,"magnitude":abs(x+1),"backend":self.name}

class VoidCPU:
    name="void-cpu"
    def run(self, state, field):
        target=state["target"]; c=field["candidate"]
        delta=target-c
        return {"delta":delta,"valid":abs(delta)<=state["tolerance"],"counter":"HOLD" if delta==0 else ("EXPRESS" if delta>0 else "COMPRESS"),"backend":self.name}

def resolve(state, field, void):
    if void["valid"]: return {"decision":"HOLD","next":field["candidate"],"done":True}
    step=1 if void["delta"]>0 else -1
    return {"decision":"ROUTE","next":field["candidate"]+step-1,"done":False}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--cycles",type=int,default=6); p.add_argument("--target",type=int,default=4); p.add_argument("--jsonl")
    a=p.parse_args(); limit=max(1,min(a.cycles,64)); state={"value":0,"target":a.target,"tolerance":0,"source":"test"}
    field,void=FieldCPU(),VoidCPU(); out=[]
    for cycle in range(limit):
        f=field.run(state); v=void.run(state,f); r=resolve(state,f,v)
        receipt={"schema":"one-wave-loop-receipt/v1","cycle":cycle,"input":state,"field":f,"void":v,"resolution":r}
        receipt["receipt_id"]=digest(receipt); out.append(receipt); print(json.dumps(receipt))
        state={**state,"value":r["next"]}
        if r["done"]: break
    if a.jsonl:
        with open(a.jsonl,"w") as h:
            for x in out: h.write(json.dumps(x,sort_keys=True)+"\n")
if __name__=="__main__": main()
