#!/usr/bin/env python3
import json, sys
from pathlib import Path

def normalize_turn(actor,payload):
    if not isinstance(payload,dict): raise ValueError("turn payload must be object")
    return {"actor":actor,"answer":str(payload.get("answer","")),
            "settled":list(payload.get("settled",[])),
            "unresolved":list(payload.get("unresolved",[])),
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
        if turn["complete"] and not unresolved and len(history)>=2 and history[-2]["complete"]:
            break
    status="COMPLETE" if len(history)>=2 and history[-1]["complete"] and history[-2]["complete"] and not unresolved else "HOLD"
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
