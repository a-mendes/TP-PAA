import algorithms.dynamic_programming as dp
import utils as ut

def experiment_1_dynamic_programming():

    instance_start = ut.last_instance_executed(1, ut.c.DYANMIC_PROGRAMMING)

    for i in range(instance_start + 1, 21):
        print(f"Instance {i}")
        dp.backpack_dynamic_programing(1, i)

def main():
    print("Experiment 1 - Dynamic Programming")
    experiment_1_dynamic_programming()

if __name__ == "__main__":
    main()