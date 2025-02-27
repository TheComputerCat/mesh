import unittest
import src.utils as utils

def checker1(M_D1, M_D2):
    return M_D1 != M_D2

def checker2(a, b):
    return a == b

class TestUtils(unittest.TestCase):

    def test_rulen_name_to_date(self):
        self.assertEqual(utils.get_shift_times("M_N"), [0, 8])
        self.assertEqual(utils.get_shift_times("M_D1"), [8, 16])
        self.assertEqual(utils.get_shift_times("T_N"), [24, 32])
        self.assertEqual(utils.get_shift_times("SU_N"), [144, 152])
        self.assertEqual(utils.get_shift_times("F_D2"), [101, 109])

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