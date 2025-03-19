import algorithms.dynamic_programming as dp
import utils as ut

def experiment_dynamic_programming(experiment):

    instance_start = ut.last_instance_executed(experiment, ut.c.DYANMIC_PROGRAMMING)
    if(instance_start == 0):
        ut.delete_logs(experiment, ut.c.DYANMIC_PROGRAMMING);

    for i in range(instance_start + 1, 21):
        print(f"Instance {i}")
        dp.backpack_dynamic_programing(experiment, i)

def main():
    #print("Experiment 1 - Dynamic Programming")
    #experiment_dynamic_programming(1)

    print("Experiment 2 - Dynamic Programming")
    experiment_dynamic_programming(2)

if __name__ == "__main__":
    main()