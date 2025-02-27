# Solving a CSP
This is a work-in-progress implementation of a CSP solver for clinic shift scheduling.
## How to Run the Code:

1. **Generate the Constraint Function Code:**
   Run the following command to generate the constraint functions:
```bash
   $ python3 -m src.constraints_creator
```
2. **Run the Solver:** After generating the constraints, run the solver with the command:
```bash
    $ python3 CSP.py
```
This will output a solution to the CSP.

Note: Not all rules have been implemented yet.
3. Run test and debug
You can run the test with
```bash
    $ python3 -m unittest tests.[file]
```
You can debug the code with:
```bash
    $ python -m debugpy --listen 5678 --wait-for-client -m unittest tests.[file]
```
And the attach a debugpy client.
If you run the code inside docker:
```bash
    $ python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m unittest tests.[file]
```
