import utils as ut
import consts as c
import numpy as np
import time

def knapsack_branch_and_bound(W, items):
    n = len(items)
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)

    def bound(i, w, v):
        if w > W:
            return 0
        while i < n and items[i][0] <= W - w:
            v += items[i][1]
            w += items[i][0]
            i += 1
        if i < n:
            v += (W - w) * items[i][1] / items[i][0]
        return v

    def branch_and_bound(i, w, v):
        nonlocal best_value
        if w > W:
            return
        best_value = max(best_value, v)
        if i == n:
            return
        if bound(i, w, v) <= best_value:
            return
        branch_and_bound(i + 1, w + items[i][0], v + items[i][1])
        branch_and_bound(i + 1, w, v)

    best_value = 0
    branch_and_bound(0, 0, 0)

    return best_value

def execute(experiment, instance):
    W, items = ut.read_instance(experiment, instance)
    
    start_time = time.time()
    solution = knapsack_branch_and_bound(W, items)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

    log_tuple = (W, len(items), execution_time)

    ut.save_logs(experiment, instance, c.BRANCH_AND_BOUND, c.EXECUTION_TIME, log_tuple)
    ut.save_logs(experiment, instance, c.BRANCH_AND_BOUND, c.SOLUTION_VALUE, solution)
    ut.save_logs(experiment, instance, c.BRANCH_AND_BOUND, c.LAST_INSTANCE_EXECUTED, instance, 'w')

    return solution
    
