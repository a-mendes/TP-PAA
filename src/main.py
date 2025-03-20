import algorithms.dynamic_programming as dp
import algorithms.branch_and_bound as bd
import utils as ut

def experiment_dynamic_programming(experiment):
    instance_start = ut.last_instance_executed(experiment, ut.c.DYNAMIC_PROGRAMMING)
    if(instance_start == 0):
        ut.delete_logs(experiment, ut.c.DYNAMIC_PROGRAMMING)

    # for i in range(instance_start + 1, 21):
    for i in range(instance_start + 1, 10):
        print(f"Instance {i}")
        dp.execute(experiment, i)

def experiment_branch_and_bound(experiment):
    instance_start = ut.last_instance_executed(experiment, ut.c.BRANCH_AND_BOUND)
    if(instance_start == 0):
        ut.delete_logs(experiment, ut.c.BRANCH_AND_BOUND)

    # for i in range(instance_start + 1, 21):
    for i in range(instance_start + 1, 10):
        print(f"Instance {i}")
        bd.execute(experiment, i)

def experiment_backtracking(experiment):
    pass

def start_experiments(experiment):
    experiment_dynamic_programming(experiment)
    experiment_branch_and_bound(experiment)
    experiment_backtracking(experiment)


def main():
    print("Experiment 1")
    start_experiments(1)

    print("Experiment 2")
    start_experiments(1)

if __name__ == "__main__":
    main()