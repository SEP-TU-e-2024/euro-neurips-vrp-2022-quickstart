# Controller has an environment and tests it against a dynamic solver program
import argparse
import tools
import json
import sys
import numpy as np
from environment import VRPEnvironment


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", help="Instance to solve")

    args = parser.parse_args(sys.argv[1:])

    # Load instance
    static_instance = tools.read_vrplib(args.instance)

    # Create environment
    env = VRPEnvironment(1, static_instance, 120, True)
    env.reset()

    # Load solution to validate from STDIN
    solution_json = json.loads(input())
    solution = [np.array(route) for route in solution_json]
    
    observation, reward, done, info = env.step(solution)
    print('---- Static Solution Verification ----')
    print(f'Observation: {observation}')
    print(f'Reward: {reward}')
    print(f'Done: {done}')
    print(f'Info: {info}')
    print(f"Cost of solution: {sum(env.final_costs.values())}")
