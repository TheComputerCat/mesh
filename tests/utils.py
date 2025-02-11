import unittest
import src.utils as utils

def checker1(M_D1, M_D2):
    return M_D1 != M_D2

def checker2(M_D1, M_E1):
    return M_D1 == M_E1

class TestUtils(unittest.TestCase):

    def test_index_to_rule_name(self):
        self.assertEqual(utils.indexVariableToNamed(0), "M_N")
        self.assertEqual(utils.indexVariableToNamed(5), "T_N")
        self.assertEqual(utils.indexVariableToNamed(34), "SU_E2")

    def test_rulen_name_to_date(self):
        self.assertEqual(utils.get_shift_times("M_N"), [23, 7])
        self.assertEqual(utils.get_shift_times("M_D1"), [7, 15])

    def test_assignment_checker(self):
        constraint_functions = {
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
        self.assertFalse(utils.check_assignment_satisfaction({ "M_D1": 1 , "M_D2":1, "M_E1":1}, constraint_functions))
        self.assertTrue(utils.check_assignment_satisfaction({ "M_D1": 1 , "M_D2":2, "M_E1":1}, constraint_functions))

if __name__ == '__main__':
    unittest.main()