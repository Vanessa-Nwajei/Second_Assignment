def fibonacci_rabbits(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[0][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][m]    

n = 6
m = 3
print(fibonacci_rabbits(n,m))