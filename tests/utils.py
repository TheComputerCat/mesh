import unittest
import src.utils as utils

def checker1(M_D1, M_D2):
    return M_D1 != M_D2

def checker2(M_D1, M_E1):
    return M_D1 == M_E1

class TestUtils(unittest.TestCase):

    def testNumToRuleName(self):
        self.assertEqual(utils.conVars(0), "M_N")
        self.assertEqual(utils.conVars(5), "T_N")
        self.assertEqual(utils.conVars(34), "SU_E2")

    def testRuleNameToDate(self):
        self.assertEqual(utils.dates("M_N"), [23, 7])
        self.assertEqual(utils.dates("M_D1"), [7, 15])

    def testAssignmentChecker(self):
        constrainFunctions = {
            "checker1": {
                "fun": checker1,
                "variables": ["M_D1", "M_D2"]
            },
            "checker2": {
                "fun": checker2,
                "variables": ["M_D1", "M_E1"]
            },
            "checker3": {
                "fun": lambda M_D1, M_D2, M_E1: M_D1 + M_D2 + M_E1 == 4,
                "variables": ["M_D1", "M_D2", "M_E1"]
            }
        }
        self.assertFalse(utils.checkSatisfy({ "M_D1": 1 , "M_D2":1, "M_E1":1}, constrainFunctions))
        self.assertTrue(utils.checkSatisfy({ "M_D1": 1 , "M_D2":2, "M_E1":1}, constrainFunctions))

if __name__ == '__main__':
    unittest.main()