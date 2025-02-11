from constraint import *
from src.constraints import conVars

problem = Problem()

physicians = range(10)

for i in range(35):
    problem.addVariable(conVars(i), physicians)



# def const1(a, b):
#     return a*2 == b

# problem.addConstraint(const1)
# solution = problem.getSolutions()
# print(solution)
