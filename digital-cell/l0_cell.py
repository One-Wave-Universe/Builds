#!/usr/bin/env python3
import json, sys
from dataclasses import dataclass, asdict
from pathlib import Path

VALID_SOURCE={"real","simulated","test"}

@dataclass(frozen=True)
class CellInput:
    field: float
    void: float
    threshold: float
    source: str="test"

def parse(obj):
    required={"field","void","threshold"}
    missing=required-set(obj)
    if missing: raise ValueError("missing: "+",".join(sorted(missing)))
    field=float(obj["field"]); void=float(obj["void"]); threshold=float(obj["threshold"])
    source=obj.get("source","test")
    if threshold <= 0: raise ValueError("threshold must be > 0")
    if source not in VALID_SOURCE: raise ValueError("source must be real|simulated|test")
    return CellInput(field,void,threshold,source)

def resolve(inp):
    d=inp.field-inp.void
    state="POSITIVE" if d>inp.threshold else "NEGATIVE" if d < -inp.threshold else "HOLD"
    return d,state

def step(obj):
    inp=parse(obj); d,state=resolve(inp)
    state_obj={"schema":"one-wave-digital-cell-state/v1","field":inp.field,"void":inp.void,
               "difference":d,"threshold":inp.threshold,"resolution":state,"source":inp.source}
    receipt={"schema":"one-wave-digital-cell-receipt/v1","input":asdict(inp),
             "transition":{"from":"OBSERVE","through":["FIELD","VOID","DIFF","LEAN"],"to":state},
             "output":state_obj,
             "dcacrc_ir":{"REFERENCE":0.0,"DIFF":["FIELD","VOID"],"LEAN":{"threshold":inp.threshold}}}
    return state_obj,receipt

def main():
    if len(sys.argv)!=2: raise SystemExit("usage: l0_cell.py fixture.json")
    obj=json.loads(Path(sys.argv[1]).read_text())
    state,receipt=step(obj)
    print(json.dumps(state,sort_keys=True))
    print(json.dumps(receipt,sort_keys=True))

if __name__=="__main__": main()
