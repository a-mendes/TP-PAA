import utils as ut

def backpack_dynamic_programing(experiment, instance):
    W, items = ut.read_instance(experiment, instance)
    return dynamic_programming(W, items)

def dynamic_programming(W, items):
    n = len(items)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            wi, vi = items[i - 1]
            if wi <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
