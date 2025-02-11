def indexVariableToNamed(i):
    if i > 34 or i < 0:
        raise "Variable out of range"
    days = ['M', 'T', 'W', 'TH', 'F', 'S', 'SU']
    shifts = ['N', 'D1', 'D2', 'E1', 'E2']
    return "{}_{}".format(days[i//5], shifts[i%5])

def get_shift_times(rule):
    _, shift = rule.split("_")
    return {'N': [23, 7], 'D1': [7, 15], 'D2': [5, 13], 'E1': [15, 23], 'E2':[13, 21] }[shift]

def check_assignment_satisfaction(assignment, constraint_functions):
    is_satisfied = True
    for CF in constraint_functions:
        fun = constraint_functions[CF]['fun']
        variables = constraint_functions[CF]['variables']
        args = {k: assignment[k] for k in assignment if k in variables}
        is_satisfied = is_satisfied and fun(**args)
        if not is_satisfied:
            return False

    return is_satisfied