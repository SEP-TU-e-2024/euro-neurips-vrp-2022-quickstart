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

To get a dummy static solution, [run the Verifier for a Solver](#verifier-for-solver-static-problem), this will print its solution at the end of the verification.

For example, the following is a Static Solution for the problem instance data in `instances/ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35.txt`:
```
[[197, 149, 259, 304, 244, 282, 240, 37, 24], [152, 350, 25, 195, 129, 361, 394, 86, 101, 46, 92, 53, 130, 105], [337, 273, 412, 291, 68, 126, 36, 100, 452, 296, 292, 448, 437, 321, 203, 95, 182], [144, 232, 230, 19, 142, 81, 257, 164, 175, 253, 307, 393, 403, 373, 85, 147], [426, 455, 184, 29, 407, 421, 262, 252, 409, 264, 430, 450, 439, 102, 204, 4, 317, 279, 212], [77, 103, 59, 155, 110, 124, 319], [401, 416, 434, 433, 413, 315, 118, 278, 233, 228, 213, 20, 15, 208, 64, 150, 167, 196], [357, 384, 418, 411, 211, 387, 67, 17, 3, 179, 301, 174, 389, 11, 109, 327, 329, 254, 286, 112], [255, 390, 241, 30, 181, 303, 91, 168, 154, 187, 370, 89, 335, 342, 428, 176, 442, 238, 156], [193, 185, 191, 247, 349, 133, 40, 114, 84, 16, 313, 227, 111, 289, 237, 218, 353, 348, 356, 355], [44, 422, 351, 368, 369, 66, 65, 298, 382, 322, 270, 243, 280, 277, 231, 225, 226, 26, 260], [106, 60, 70, 139, 121, 385, 432, 170, 214, 310, 79, 306, 123, 127, 138, 153, 140], [263, 249, 234, 135, 235, 354, 314, 324, 54, 47, 376, 94, 96, 122, 117, 104], [206, 283, 224, 400, 48, 132, 188, 272, 223, 217, 207, 210, 209, 340, 358, 163, 371, 388, 311, 320], [21, 162, 173, 386, 219, 229, 265, 269, 14, 183, 436, 201, 18, 13, 12, 137, 43, 134, 205, 148], [190, 316, 136, 165, 202, 186, 87, 2, 5, 345, 281, 61, 364, 449, 6, 261, 456, 446, 198, 22, 189], [268, 445, 1, 200, 415, 245, 397, 395, 431, 35, 447, 145, 276, 275, 274, 297, 312], [392, 396, 166, 417, 169, 119, 28, 34, 45, 39, 31, 427, 248], [379, 429, 336, 318, 300, 8, 7, 295, 443, 408, 398, 294, 293, 32, 305, 362, 367, 420, 347, 457, 404], [323, 333, 328, 33, 341, 299, 57, 435, 423, 288, 287, 365, 50, 419], [69, 271, 346, 215, 267, 159, 160, 338, 256, 343, 251, 309, 258, 326, 414, 372], [99, 410, 374, 381, 406, 441, 62, 141, 180, 266, 246, 220, 194, 454, 440, 402, 451, 458], [405, 71, 75, 76, 151, 55, 88, 83, 52, 344, 339, 63, 27, 172, 334, 332, 222, 308], [375, 49, 58], [366, 125, 80], [42, 284, 359, 9, 330, 438, 98, 41, 73, 56, 131, 116, 290], [171, 285, 10, 239, 157, 250, 74, 178, 51, 236, 216, 199, 221, 82, 143, 192, 120, 444], [108, 107, 72, 93, 97, 146, 242, 331, 113, 38, 425, 161, 325, 383, 360, 78, 177, 158, 399, 453], [352, 23, 302, 115, 90, 128, 391, 377, 378, 380, 424, 363]]
```