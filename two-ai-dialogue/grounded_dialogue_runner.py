#!/usr/bin/env python3
"""Bounded visible-turn Brain Buddy runner.

All actors receive the same immutable repository evidence pack. The default
three-peer cycle is CHATGPT -> GEMINI -> DEEPSEEK. Only visible answers and
provider/model/response provenance are stored.
"""
import json, pathlib, subprocess, sys, tempfile
HERE=pathlib.Path(__file__).resolve().parent
ALLOWED={"CHATGPT","GEMINI","DEEPSEEK"}
ADAPTERS={"CHATGPT":"openai_adapter.py","GEMINI":"gemini_adapter.py","DEEPSEEK":"deepseek_adapter.py"}

def invoke(adapter, packet):
    with tempfile.NamedTemporaryFile("w",suffix=".json",delete=False) as h:
        json.dump(packet,h); path=h.name
    try:
        p=subprocess.run([sys.executable,str(HERE/adapter),path],text=True,capture_output=True,timeout=240)
        raw=(p.stdout or "").strip().splitlines()
        if not raw:return {"status":"HOLD","error":(p.stderr or "empty adapter output")[-2000:]}
        try:return json.loads(raw[-1])
        except Exception:return {"status":"HOLD","error":"adapter returned non-JSON","raw":(p.stdout or "")[-4000:]}
    finally:pathlib.Path(path).unlink(missing_ok=True)

def validate_actors(actors):
    if not isinstance(actors,list) or len(actors)<2 or any(a not in ALLOWED for a in actors):
        raise ValueError("actors must be a list of CHATGPT/GEMINI/DEEPSEEK")
    if len(set(actors))!=len(actors):raise ValueError("actors must be unique")
    return actors

def run(req):
    rid=req["id"]; question=req["question"]; max_turns=max(2,min(int(req.get("max_turns",6)),12))
    actors=validate_actors(req.get("actors",["CHATGPT","GEMINI","DEEPSEEK"]))
    evidence=req.get("evidence_pack","repo-evidence.json")
    history=[]; previous=""; settled=[]; unresolved=[question]
    for n in range(max_turns):
        actor=actors[n%len(actors)]
        packet={"id":rid,"question":question,"previous_visible_answer":previous,
          "visible_history":history,"settled":settled,"unresolved":unresolved,
          "evidence_pack":evidence,"dialogue_turn":n+1,"dialogue_actor":actor}
        receipt=invoke(ADAPTERS[actor],packet)
        if receipt.get("status")!="COMPLETE":
            return {"schema":"one-wave-grounded-dialogue/v2","id":rid,"status":"HOLD","turns":history,
              "last_successful_actor":history[-1]["actor"] if history else None,
              "last_successful_answer":history[-1]["answer"] if history else "",
              "blocker":{"actor":actor,"receipt":receipt}}
        turn=receipt["turn"]
        visible={"turn":n+1,"actor":actor,"answer":turn.get("answer",""),"provider":turn.get("provider"),
          "model":turn.get("model"),"response_id":turn.get("response_id"),"receipt_status":"COMPLETE"}
        history.append(visible);previous=visible["answer"]
    return {"schema":"one-wave-grounded-dialogue/v2","id":rid,"status":"MAX_TURNS",
      "actors":actors,"turns":history,"final_visible_answer":history[-1]["answer"] if history else ""}

if __name__=="__main__":
    if len(sys.argv)!=2:raise SystemExit("usage: grounded_dialogue_runner.py REQUEST.json")
    print(json.dumps(run(json.loads(pathlib.Path(sys.argv[1]).read_text())),indent=2))
