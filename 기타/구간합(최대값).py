scores = [-14, 7, 2, 10, -4, 9, -10]

def partial_sum_dp(scores):
    dp = [0] * len(scores)
    dp[0] = scores[0]
    for i in range(len(scores)):
        dp[i] = max(0, dp[i-1]) + scores[i]
        print('idx: {}, score : {} \ndp : {} '.format(i, scores[i], dp))
    return max(dp)


print(partial_sum_dp(scores))
