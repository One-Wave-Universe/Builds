#!/usr/bin/env python3
"""Bounded visible-turn dialogue runner for the proven grounded peer lane.

Runs only after repo-evidence.json has been built from One-Wave-Science.
It alternates CHATGPT <-> GEMINI under one request ID and stores only visible
answers plus provider/model/response provenance. No hidden reasoning is requested.
"""
import json, os, pathlib, subprocess, sys, tempfile

HERE=pathlib.Path(__file__).resolve().parent

def invoke(adapter, packet):
    with tempfile.NamedTemporaryFile("w",suffix=".json",delete=False) as h:
        json.dump(packet,h); path=h.name
    try:
        p=subprocess.run([sys.executable,str(HERE/adapter),path],text=True,capture_output=True,timeout=240)
        raw=(p.stdout or "").strip().splitlines()
        if not raw:
            return {"status":"HOLD","error":(p.stderr or "empty adapter output")[-2000:]}
        try: return json.loads(raw[-1])
        except Exception:
            return {"status":"HOLD","error":"adapter returned non-JSON","raw":(p.stdout or "")[-4000:]}
    finally:
        pathlib.Path(path).unlink(missing_ok=True)

def run(req):
    rid=req["id"]; question=req["question"]; max_turns=max(2,min(int(req.get("max_turns",4)),8))
    peer_order=req.get("actors",["CHATGPT","GEMINI"])
    if peer_order!=["CHATGPT","GEMINI"]:
        raise ValueError("actors must be [CHATGPT,GEMINI] for v1")
    evidence=req.get("evidence_pack","repo-evidence.json")
    history=[]; previous=""; settled=[]; unresolved=[question]
    adapters={"CHATGPT":"openai_adapter.py","GEMINI":"gemini_adapter.py"}
    for n in range(max_turns):
        actor=peer_order[n%2]
        packet={
          "id":rid,
          "question":question,
          "previous_visible_answer":previous,
          "settled":settled,
          "unresolved":unresolved,
          "evidence_pack":evidence,
          "dialogue_turn":n+1,
          "dialogue_actor":actor,
        }
        receipt=invoke(adapters[actor],packet)
        if receipt.get("status")!="COMPLETE":
            return {"schema":"one-wave-grounded-dialogue/v1","id":rid,"status":"HOLD",
                    "turns":history,"blocker":{"actor":actor,"receipt":receipt}}
        turn=receipt["turn"]
        visible={"turn":n+1,"actor":actor,"answer":turn.get("answer",""),
                 "provider":turn.get("provider"),"model":turn.get("model"),
                 "response_id":turn.get("response_id"),"receipt_status":"COMPLETE"}
        history.append(visible); previous=visible["answer"]
    return {"schema":"one-wave-grounded-dialogue/v1","id":rid,"status":"MAX_TURNS",
            "turns":history,"final_visible_answer":history[-1]["answer"] if history else ""}

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: grounded_dialogue_runner.py REQUEST.json")
    req=json.loads(pathlib.Path(sys.argv[1]).read_text())
    print(json.dumps(run(req),indent=2))
