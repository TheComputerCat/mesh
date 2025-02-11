def conVars(i):
    if i > 34 or i < 0:
        raise "Variable out of range"
    days = ['M', 'T', 'W', 'TH', 'F', 'S', 'SU']
    shifts = ['N', 'D1', 'D2', 'E1', 'E2']
    return "{}_{}".format(days[i//5], shifts[i%5])

def dates(rule):
    _, shift = rule.split("_")
    return {'N': [23, 7], 'D1': [7, 15], 'D2': [5, 13], 'E1': [15, 23], 'E2':[13, 21] }[shift]

def checkSatisfy(assignment, constrainFunctions):
    satisfy = True
    for CF in constrainFunctions:
        fun = constrainFunctions[CF]['fun']
        domain = constrainFunctions[CF]['domain']
        args = {k: assignment[k] for k in assignment if k in domain}
        satisfy = satisfy and fun(**args)
        if not satisfy:
            return False

    return satisfy