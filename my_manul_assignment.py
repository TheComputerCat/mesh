from src.utils import check_assignment_satisfaction
from generated.constrains import constraint_functions
assignment = {
    "M_N": 1,
    "M_D1":2,
    "M_D2":4,
    "M_E1":3,
    "M_E2":5,

    "T_N": 3,
    "T_D1":2,
    "T_D2":4,
    "T_E1":1,
    "T_E2":5,

    "W_N": 1,
    "W_D1":5,
    "W_D2":3,
    "W_E1":2,
    "W_E2":4,

    "TH_N": 2,
    "TH_D1":4,
    "TH_D2":3,
    "TH_E1":1,
    "TH_E2":5,

    "F_N": 1,
    "F_D1":5,
    "F_D2":4,
    "F_E1":2,
    "F_E2":3,

    "S_N": 2,
    "S_D1":3,
    "S_D2":4,
    "S_E1":1,
    "S_E2":5,

    "SU_N": 1,
    "SU_D1":5,
    "SU_D2":4,
    "SU_E1":3,
    "SU_E2":2
}

print(check_assignment_satisfaction(assignment, constraint_functions))