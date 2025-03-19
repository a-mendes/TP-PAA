import os
import random
from consts import *

def generate_experiment_1():
    n = 100
    for i in range(1, 21):
        W = 100  
        items = [(random.randint(1, WEIGHT_MAX), random.randint(1, VALUE_MAX)) for _ in range(n)] 

        filename = f'{EXPERIMENT_1_DIR}/{i}.txt'
        
        with open(filename, 'w') as f:
            f.write(f"{W}\n")
            for wi, vi in items:
                f.write(f"{wi}\t{vi}\n")
        
        print(f"Generated {filename}")
        
        n *= 2

def generate_experiment_2():
    n = 400
    W = 100
    for i in range(1, 21):
        items = [(random.randint(1, WEIGHT_MAX), random.randint(1, VALUE_MAX)) for _ in range(n)]  

        filename = f'{EXPERIMENT_2_DIR}/{i}.txt'
        
        with open(filename, 'w') as f:
            f.write(f"{W}\n")
            for wi, vi in items:
                f.write(f"{wi}\t{vi}\n")

        print(f"Generated {filename}")
        
        W *= 2

def generate_instances():
    print("Generating instances...")

    if not os.path.exists('instances'):
        os.makedirs('instances')
    if not os.path.exists(EXPERIMENT_1_DIR):
        os.makedirs(EXPERIMENT_1_DIR)
    if not os.path.exists(EXPERIMENT_2_DIR):
        os.makedirs(EXPERIMENT_2_DIR)

    print("Generating experiment 1 instances...")
    generate_experiment_1()

    print("Generating experiment 2 instances...")
    generate_experiment_2()

    print("Successfully generated instances")

if __name__ == "__main__":
    generate_instances()