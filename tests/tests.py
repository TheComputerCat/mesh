import unittest
import src.constraints as constraints

def checker1(M_D1, M_D2):
    return M_D1 != M_D2

def checker2(M_D1, M_E1):
    return M_D1 == M_E1

class TestStringMethods(unittest.TestCase):

    def testNumToRuleName(self):
        self.assertEqual(constraints.conVars(0), "M_N")
        self.assertEqual(constraints.conVars(5), "T_N")
        self.assertEqual(constraints.conVars(34), "SU_E2")

    def testRuleNameToDate(self):
        self.assertEqual(constraints.dates("M_N"), [23, 7])
        self.assertEqual(constraints.dates("M_D1"), [7, 15])

    def testAssignmentChecker(self):
        constrainFunctions = {
            "checker1": {
                "fun": checker1,
                "domain": ["M_D1", "M_D2"]
            },
            "checker2": {
                "fun": checker2,
                "domain": ["M_D1", "M_E1"]
            }
        }
        self.assertFalse(constraints.checkSatisfy({ "M_D1": 1 , "M_D2":1, "M_E1":1}, constrainFunctions))
        self.assertTrue(constraints.checkSatisfy({ "M_D1": 1 , "M_D2":2, "M_E1":1}, constrainFunctions))

if __name__ == '__main__':
    unittest.main()