import utils as ut
import consts as c
import numpy as np
import time

def backpack_dynamic_programing(experiment, instance):
    W, items = ut.read_instance(experiment, instance)
    
    start_time = time.time()
    solution = dynamic_programming(W, items)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

    log_tuple = (len(items), execution_time)

    ut.save_logs(experiment, instance, c.DYANMIC_PROGRAMMING, c.EXECUTION_TIME, log_tuple)
    ut.save_logs(experiment, instance, c.DYANMIC_PROGRAMMING, c.SOLUTION_VALUE, solution)
    ut.save_logs(experiment, instance, c.DYANMIC_PROGRAMMING, c.LAST_INSTANCE_EXECUTED, instance, 'w')

    return solution

def dynamic_programming(W, items):
    
    n = len(items)
    dp = np.zeros((n + 1, W + 1), dtype=int)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            wi, vi = items[i - 1]
            if wi <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
