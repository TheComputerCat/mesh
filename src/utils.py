VARIABLES = [
    "M_N", "M_D1", "M_D2", "M_E1", "M_E2",
    "T_N", "T_D1", "T_D2", "T_E1", "T_E2",
    "W_N", "W_D1", "W_D2", "W_E1", "W_E2",
    "TH_N", "TH_D1", "TH_D2", "TH_E1", "TH_E2",
    "F_N", "F_D1", "F_D2", "F_E1", "F_E2",
    "S_N", "S_D1", "S_D2", "S_E1", "S_E2",
    "SU_N", "SU_D1", "SU_D2", "SU_E1", "SU_E2"
]

DAYS = ['M', 'T', 'W', 'TH', 'F', 'S', 'SU']

SHIFT_LONG= 8

def get_shift_times(rule):
    day, shift = rule.split("_")
    absolute_start_time = {'N': 0, 'D1': 8, 'D2': 5, 'E1': 16, 'E2':13 }[shift]
    offset = 24*DAYS.index(day)
    return [t := absolute_start_time + offset, t + SHIFT_LONG]

def check_assignment_satisfaction(assignment, constraint_functions):
    is_satisfied = True
    for CF in constraint_functions:
        fun = constraint_functions[CF]['fun']
        variables = constraint_functions[CF]['variables']
        args = (assignment[k] for k in assignment if k in variables)
        is_satisfied = is_satisfied and fun(*args)
        if not is_satisfied:
            return False

    return is_satisfied

def variables_with_shared_time(): # This could be more general
    variables = []
    formatter = lambda day: [[f"{day}_N", f"{day}_D2"], [f"{day}_D1", f"{day}_D2"], [f"{day}_D1", f"{day}_E2"], [f"{day}_E1", f"{day}_E2"]]
    for day in DAYS:
        variables.extend(formatter(day))
    return variables

def is_prev_day_of(shift1, shift2):
    day1, _ = shift1.split("_")
    day2, _ = shift2.split("_")
    if DAYS.index(day1) - DAYS.index(day2) in {0, 1}:
        return True

def shifts_are_speared_by_ten_hours(shift1, shift2):
    if not is_prev_day_of(shift1, shift2):
        return False

    dS10, dS11 = get_shift_times(shift1)
    dS20, dS21 = get_shift_times(shift2)

    if dS21 > dS10 - 10 and dS21 <= dS10:
        return True
    return False

def prev(shift):
    res = []
    for var in VARIABLES:
        if shifts_are_speared_by_ten_hours(shift, var):
            res.append(var)
    return res