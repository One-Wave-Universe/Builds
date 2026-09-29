#!/usr/bin/env python3
"""Bounded repository evidence packer for peer-AI reviews.

Runs in GitHub Actions after checkout. It reads only tracked text files from
explicitly allowed repository roots, records commit/path/hash, and never gives
the provider credentials or arbitrary shell access.
"""
import argparse, hashlib, json, pathlib, subprocess

TEXT_EXT={".md",".txt",".json",".jsonl",".py",".yml",".yaml",".toml",".csv"}
PRIORITY=("README","CANON","CORRECTION","CONTRACT","GOLD","ASSUMPT","TRANSFORM","CONTROL","NULL","G-767","G-766")

def git_at(root,*a):
    return subprocess.check_output(["git","-C",root,*a],text=True).strip()

def tracked(root):
    out=git_at(root,"ls-files").splitlines()
    return [p for p in out if pathlib.Path(p).suffix.lower() in TEXT_EXT]

def score(path, terms):
    u=path.upper()
    return sum(8 for x in PRIORITY if x in u)+sum(4 for t in terms if t.upper() in u)

def pack(root, query, max_files=18, max_chars=90000):
    terms=[x for x in query.replace("/"," ").replace("_"," ").split() if len(x)>2]
    paths=tracked(root)
    # Path-priority first; then bounded content keyword scan.
    ranked=sorted(paths,key=lambda p:(-score(p,terms),p))
    selected=[]; total=0
    for p in ranked:
        try: raw=(pathlib.Path(root)/p).read_text(errors="replace")
        except OSError: continue
        hit=score(p,terms)+sum(raw.lower().count(t.lower()) for t in terms[:12])
        if hit<=0 and selected: continue
        raw=raw[:18000]
        if total+len(raw)>max_chars: continue
        selected.append({"path":p,"sha256":hashlib.sha256(raw.encode()).hexdigest(),"content":raw})
        total+=len(raw)
        if len(selected)>=max_files: break
    return {"schema":"one-wave-repo-evidence/v1","repo_root":root,"commit":git_at(root,"rev-parse","HEAD"),"query":query,
            "files":selected,"limits":{"max_files":max_files,"max_chars":max_chars},
            "instruction":"Cite inspected repository paths. If evidence is insufficient, name exact additional paths/search terms needed; do not infer unseen repository contents."}

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default=".")
    ap.add_argument("--query",required=True); ap.add_argument("--output",required=True)
    ap.add_argument("--max-files",type=int,default=18); ap.add_argument("--max-chars",type=int,default=90000)
    a=ap.parse_args()
    pathlib.Path(a.output).write_text(json.dumps(pack(a.root,a.query,a.max_files,a.max_chars),indent=2))
