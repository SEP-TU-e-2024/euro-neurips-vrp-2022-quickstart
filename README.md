# VRPTW contest 2022

Original repository can be found at https://github.com/ortec/euro-neurips-vrp-2022-quickstart.

This repository has few if any functional changes, and mostly documents how you can run a dynamic VRPTW submission, or validate a static VRPTW solution.

This document uses terminology version 4.3 as much as possible. Use the v4.3 terminology diagram for reference.

## Setup
As this is a Python project, I recommend using a virtual environment, this guide assumes you are familiar with this process. The directory name `.venv` is added to the `.gitignore` file for this purpose.

To build and install all dependencies (Python libaries and others), run `./install.sh`. This first installs the Python libraries, then builds HGS-VRPTW, the baseline solver.

## Commands
### Verifier for Solver (Static Problem)
A Solver is an algorithmic code submission. A Verifier is able to verify the correctness of a Solver for a Static Problem.

Use the command `python controller.py --instance instances/ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35.txt --epoch_tlim 5 --static -- ./run.sh`.
This will evaluate the Solver in `solver.py` (containing the baseline HGS-VRPTW Solver) with the given Problem Instance (from `--instance`). 

The `controller.py` file combined with `environment.py` (and possibly others) forms the Verifier in this repository.

### Simulator for Solver (Dynamic Problem)
A Solver is an algorithmic code submission. A Simulator is able to verify the correctness of a Solver for a Dynamic Problem.

Use the command `python controller.py --instance instances/ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35.txt --epoch_tlim 5 -- ./run.sh`.
This will evaluate the Solver in `solver.py` (containing the baseline HGS-VRPTW Solver) (using a Simulator) with the given Problem Instance (from `--instance`).

The `controller.py` file combined with `environment.py` (and possibly others) forms the Verifier in this repository.

### Verifying Static Solution (Static Problem)
A Static Solution is the output data of a Solver for a Static Problem.

Use the command `python verify_static_solution.py --instance instances/ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35.txt`.
This will read a Static Solution from standard input, and Verify it.
