#!/usr/bin/env python3
import json
from pathlib import Path
import importlib.util

HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location("l0",HERE/"l0_cell.py")
l0=importlib.util.module_from_spec(spec); spec.loader.exec_module(l0)

def parser_cell(artifact, required):
    if not isinstance(artifact,dict): raise ValueError("artifact must be object")
    if not isinstance(required,list) or not all(isinstance(x,str) and x for x in required):
        raise ValueError("required must be non-empty string names")
    present={k:artifact[k] for k in required if k in artifact}
    missing=[k for k in required if k not in artifact]
    contradictions=[k for k in required if k in artifact and artifact[k] is None]
    usable={k:v for k,v in present.items() if v is not None}
    # L0 maps expressed usable requirements against unresolved requirements.
    state,base=l0.step({"field":len(usable),"void":len(set(missing+contradictions)),
                        "threshold":0.5,"source":"test"})
    return {"schema":"one-wave-parser-cell/v1","FIELD":{"present":usable},
            "VOID":{"missing":missing,"contradicting":contradictions},
            "resolution":state["resolution"],"l0_receipt":base}

def validator_cell(candidate, contract):
    if not isinstance(candidate,dict) or not isinstance(contract,dict):
        raise ValueError("candidate and contract must be objects")
    required=contract.get("required",[])
    forbidden=contract.get("forbidden",[])
    if not isinstance(required,list) or not isinstance(forbidden,list):
        raise ValueError("contract required/forbidden must be lists")
    missing=[k for k in required if k not in candidate]
    violations=[k for k in forbidden if k in candidate]
    evidence=contract.get("evidence",[])
    missing_evidence=[k for k in evidence if not candidate.get(k)]
    if violations:
        decision="REJECT"
    elif missing or missing_evidence:
        decision="HOLD_REQUEST"
    else:
        decision="PASS"
    return {"schema":"one-wave-validator-cell/v1",
            "FIELD":{"candidate":candidate},
            "VOID":{"missing":missing,"violations":violations,"missing_evidence":missing_evidence},
            "decision":decision,
            "mutated_candidate":False}

def main(path):
    obj=json.loads(Path(path).read_text())
    mode=obj["mode"]
    out=parser_cell(obj["artifact"],obj["required"]) if mode=="parse" else validator_cell(obj["candidate"],obj["contract"]) if mode=="validate" else None
    if out is None: raise ValueError("mode must be parse|validate")
    print(json.dumps(out,sort_keys=True))

if __name__=="__main__":
    import sys
    if len(sys.argv)!=2: raise SystemExit("usage: parser_validator.py fixture.json")
    main(sys.argv[1])
