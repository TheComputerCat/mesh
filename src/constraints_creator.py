from src.utils import get_shift_times, variables_with_shared_time
import os

def only_one_shift_per_time_creator(variables):
    functionObjects = ""
    for i, variable in enumerate(variables):
        functionObject = f"""
"only_one_shift_per_time_M{i}": {{
    "fun": only_one_shift_per_time,
    "variables": ["{'", "'.join(variable)}"]
}},
"""
        functionObjects += functionObject

    return f"""
def only_one_shift_per_time(shift1,shift2):
    return shift1 != shift2

constraint_functions = {{{functionObjects}}}
"""

def create():
    if not os.path.exists("generated/"):
        os.makedirs("generated/")
    with open("generated/constrains.py", "w") as file:
        file.write(only_one_shift_per_time_creator(variables_with_shared_time()))

    print("Constraint functions created")

if __name__ == '__main__':
    create()