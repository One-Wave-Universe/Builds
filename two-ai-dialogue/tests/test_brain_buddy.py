#!/usr/bin/env python3
import importlib.util, json, pathlib, tempfile, unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
P=ROOT/"brain_buddy.py"
spec=importlib.util.spec_from_file_location("brain_buddy",P)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class A:
    id="test-1";question="Check the repo first";query="canon evidence";max_turns=4

class BrainBuddyTests(unittest.TestCase):
    def test_one_shot_contract(self):
        x=m.base_request(A(),False)
        self.assertEqual(x["peer"],"gemini")
        self.assertEqual(x["repo_read"]["repository"],m.SCIENCE_REPO)
        self.assertEqual(x["repo_read"]["root"],"peer-repo")
    def test_dialogue_contract(self):
        x=m.base_request(A(),True)
        self.assertEqual(x["actors"],["GEMINI","CHATGPT"])
        self.assertEqual(x["max_turns"],4)
    def test_receipt_id_gate(self):
        with tempfile.TemporaryDirectory() as d:
            q=pathlib.Path(d)/"q.json";r=pathlib.Path(d)/"r.json"
            q.write_text(json.dumps({"id":"abc"}))
            r.write_text(json.dumps({"request_id":"abc","status":"COMPLETE"}))
            self.assertTrue(m.verify(q,r)["ok"])
    def test_receipt_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            q=pathlib.Path(d)/"q.json";r=pathlib.Path(d)/"r.json"
            q.write_text(json.dumps({"id":"abc"}))
            r.write_text(json.dumps({"request_id":"xyz","status":"COMPLETE"}))
            with self.assertRaises(ValueError): m.verify(q,r)

if __name__=="__main__": unittest.main()
