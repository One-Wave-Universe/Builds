#!/usr/bin/env python3
import json, sys
from pathlib import Path

def normalize_turn(actor,payload):
    if not isinstance(payload,dict): raise ValueError("turn payload must be object")
    return {"actor":actor,"answer":str(payload.get("answer","")),
            "settled":list(payload.get("settled",payload.get("agreements",[]))),
            "unresolved":list(payload.get("unresolved",[])),
            "objections":list(payload.get("objections",[])),
            "proposed_resolution":payload.get("proposed_resolution"),
            "proposed_next_action":payload.get("proposed_next_action"),
            "accept_previous":bool(payload.get("accept_previous",False)),
            "complete":bool(payload.get("complete",False))}

def run(question, adapters, max_turns=8):
    if not question.strip(): raise ValueError("question required")
    history=[]; settled=[]; unresolved=[question]; actor_names=["CHATGPT","GEMINI"]
    for i in range(max_turns):
        actor=actor_names[i%2]
        payload=adapters[actor]({"question":question,"previous":history[-1] if history else None,
                                "settled":settled,"unresolved":unresolved,"turn":i+1})
        turn=normalize_turn(actor,payload); history.append(turn)
        settled=list(dict.fromkeys(settled+turn["settled"]))
        unresolved=turn["unresolved"]
        if len(history)>=2 and turn["accept_previous"]:
            prev=history[-2]
            same_resolution=bool(prev.get("proposed_resolution") and turn.get("proposed_resolution") and prev["proposed_resolution"].strip()==turn["proposed_resolution"].strip())
            same_action=bool(prev.get("proposed_next_action") and turn.get("proposed_next_action") and prev["proposed_next_action"].strip()==turn["proposed_next_action"].strip())
            if same_resolution or same_action:
                unresolved=[]
                break
    status="HOLD"
    if len(history)>=2 and history[-1].get("accept_previous") and not unresolved:
        prev,last=history[-2],history[-1]
        if prev.get("proposed_resolution") and prev.get("proposed_resolution")==last.get("proposed_resolution"):
            status="AGREED_RESOLUTION"
        elif prev.get("proposed_next_action") and prev.get("proposed_next_action")==last.get("proposed_next_action"):
            status="AGREED_NEXT_ACTION"
    if status=="HOLD" and len(history)>=max_turns:
        status="MAX_TURNS"
    return {"schema":"one-wave-two-ai-dialogue/v1","question":question,"status":status,
            "turns":history,"settled":settled,"unresolved":unresolved,
            "final":history[-1]["answer"] if history else ""}

def fixture_adapter(name, scripted):
    state={"i":0}
    def call(_):
        xs=scripted[name]; x=xs[min(state["i"],len(xs)-1)]; state["i"]+=1; return x
    return call

def main(path):
    x=json.loads(Path(path).read_text())
    adapters={n:fixture_adapter(n,x["scripted"]) for n in ("CHATGPT","GEMINI")}
    print(json.dumps(run(x["question"],adapters,x.get("max_turns",8)),sort_keys=True))
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: loop.py fixture.json")
    main(sys.argv[1])
