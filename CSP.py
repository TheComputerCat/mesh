from constraint import *
from src.utils import VARIABLES
from generated.constrains import constraint_functions

problem = Problem()
physicians = range(10)

for shift in VARIABLES:
    problem.addVariable(shift, physicians)

for constraint in constraint_functions.values():
    problem.addConstraint(constraint["fun"], constraint["variables"])
solution = problem.getSolution()
print(solution)
