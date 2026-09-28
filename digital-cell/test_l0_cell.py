import importlib.util, json, unittest
from pathlib import Path
HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location("l0",HERE/"l0_cell.py")
l0=importlib.util.module_from_spec(spec); spec.loader.exec_module(l0)

class L0Tests(unittest.TestCase):
    def fixture(self,name): return json.loads((HERE/"fixtures"/name).read_text())
    def test_positive(self): self.assertEqual(l0.step(self.fixture("positive.json"))[0]["resolution"],"POSITIVE")
    def test_negative(self): self.assertEqual(l0.step(self.fixture("negative.json"))[0]["resolution"],"NEGATIVE")
    def test_hold_opposition(self): self.assertEqual(l0.step(self.fixture("hold.json"))[0]["resolution"],"HOLD")
    def test_malformed(self):
        with self.assertRaises(ValueError): l0.step(self.fixture("malformed.json"))
    def test_deterministic_replay(self):
        x=self.fixture("positive.json")
        self.assertEqual(l0.step(x),l0.step(x))
    def test_json_roundtrip(self):
        state,receipt=l0.step(self.fixture("negative.json"))
        self.assertEqual(json.loads(json.dumps(state)),state)
        self.assertEqual(json.loads(json.dumps(receipt)),receipt)

if __name__=="__main__": unittest.main()
