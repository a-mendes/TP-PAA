import utils as ut
import consts as c
import time

def execute(experiment, instance):
    W, items = ut.read_instance(experiment, instance)
    
    start_time = time.time()
    solution = backtracking(W, items)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")

    log_tuple = (W, len(items), execution_time)

    ut.save_logs(experiment, instance, c.BACKTRACKING, c.EXECUTION_TIME, log_tuple)
    ut.save_logs(experiment, instance, c.BACKTRACKING, c.SOLUTION_VALUE, solution)
    ut.save_logs(experiment, instance, c.BACKTRACKING, c.LAST_INSTANCE_EXECUTED, instance, 'w')

    return solution

def alg_backtracking(W, items):
    n = len(items)
    best_value = [0]  # Usamos uma lista para manter o valor máximo atualizado

    def backtrack(i, current_weight, current_value):
        if current_weight > W:
            return
        best_value[0] = max(best_value[0], current_value)
        if i == n:
            return
        # Escolhe o item atual
        backtrack(i + 1, current_weight + items[i][0], current_value + items[i][1])
        # Não escolhe o item atual
        backtrack(i + 1, current_weight, current_value)
    
    backtrack(0, 0, 0)
    return best_value[0]