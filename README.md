# VRPTW contest 2022

Original repository can be found at https://github.com/ortec/euro-neurips-vrp-2022-quickstart.

This repository has few if any functional changes, and mostly documents how you can run a dynamic VRPTW submission, or validate a static VRPTW solution.

## Setup
As this is a Python project, I recommend using a virtual environment, this guide assumes you are familiar with this process. The directory name `.venv` is added to the `.gitignore` file for this purpose.

To build and install all dependencies (Python libaries and others), run `./install.sh`. This first installs the Python libraries, then builds HGS-VRPTW, the baseline solver.

