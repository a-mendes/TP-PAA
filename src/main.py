import algorithms.dynamic_programming as dp
import algorithms.branch_and_bound as bd
import algorithms.backtracking as bt
import utils as ut

def experiment_dynamic_programming(experiment):
    print("\nDynamic programming\n")
    instance_start = ut.last_instance_executed(experiment, ut.c.DYNAMIC_PROGRAMMING)
    if(instance_start == 0):
        ut.delete_logs(experiment, ut.c.DYNAMIC_PROGRAMMING)

    for i in range(instance_start + 1, 21):
        print(f"Instance {i}")
        dp.execute(experiment, i)

def experiment_branch_and_bound(experiment):
    print("\nBranch and bound\n")
    instance_start = ut.last_instance_executed(experiment, ut.c.BRANCH_AND_BOUND)
    if(instance_start == 0):
        ut.delete_logs(experiment, ut.c.BRANCH_AND_BOUND)

    for i in range(instance_start + 1, 21):
        print(f"Instance {i}")
        bd.execute(experiment, i)

def experiment_backtracking(experiment):
    print("\nBacktracking\n")
    instance_start = ut.last_instance_executed(experiment, ut.c.BACKTRACKING)  
    if instance_start == 0:
        ut.delete_logs(experiment, ut.c.BACKTRACKING)  

    for i in range(instance_start + 1, 21):
        print(f"Instance {i}")
        bt.execute(experiment, i)


def plot_results(experiment):
    ut.plot_results(experiment)
    ut.plot_results(experiment)
    # ut.plot_results(experiment)

def start_experiments(experiment):
    experiment_dynamic_programming(experiment)
    experiment_branch_and_bound(experiment)
    experiment_backtracking(experiment)
    plot_results(experiment)

def main():
    print("Experiment 1")
    start_experiments(1)

    print("Experiment 2")
    start_experiments(2)

if __name__ == "__main__":
    main()