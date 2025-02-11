import unittest
import src.constraints_creator as constraints_creator
import inspect

class TestConstrainCreator(unittest.TestCase):

    def test_only_one_shift_per_time(self):
        variables = [
            ["M_N", "M_D2"],
            ["M_D1", "M_D2"]
        ]
        genCode = constraints_creator.only_one_shift_per_time_creator(variables)

        exec(genCode, globals())

        self.assertFalse(only_one_shift_per_time(1,1))
        self.assertTrue(only_one_shift_per_time(2,1))

        for i, variable in enumerate(variables):
            self.assertEqual(constraint_functions[f"only_one_shift_per_time_M{i}"]["variables"], variable)


if __name__ == '__main__':
    unittest.main()