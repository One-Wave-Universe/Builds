import importlib.util, unittest
from pathlib import Path
HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location("pv",HERE/"parser_validator.py")
pv=importlib.util.module_from_spec(spec); spec.loader.exec_module(pv)

class ParserValidatorTests(unittest.TestCase):
    def test_parser_present_missing(self):
        x=pv.parser_cell({"a":1},["a","b"])
        self.assertEqual(x["FIELD"]["present"],{"a":1})
        self.assertEqual(x["VOID"]["missing"],["b"])
    def test_parser_contradiction(self):
        x=pv.parser_cell({"a":None},["a"])
        self.assertEqual(x["VOID"]["contradicting"],["a"])
    def test_validator_pass(self):
        x=pv.validator_cell({"a":1,"receipt":"ok"},{"required":["a"],"evidence":["receipt"]})
        self.assertEqual(x["decision"],"PASS")
    def test_validator_request(self):
        x=pv.validator_cell({"a":1},{"required":["a","b"]})
        self.assertEqual(x["decision"],"HOLD_REQUEST")
    def test_validator_reject(self):
        c={"a":1,"secret":"x"}; before=dict(c)
        x=pv.validator_cell(c,{"required":["a"],"forbidden":["secret"]})
        self.assertEqual(x["decision"],"REJECT")
        self.assertEqual(c,before)
        self.assertFalse(x["mutated_candidate"])
    def test_malformed(self):
        with self.assertRaises(ValueError): pv.parser_cell([],["a"])

if __name__=="__main__": unittest.main()
