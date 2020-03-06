N = int(input())
seq = list(map(int, input().split()))

dp = [[0 for i in range(21)] for j in range(N - 1)]
dp[0][seq[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if j - seq[i] >= 0:
            dp[i][j] += dp[i - 1][j - seq[i]]
        
        if j + seq[i] <= 20:
            dp[i][j] += dp[i - 1][j + seq[i]]
        
        
print(dp[N - 2][seq[-1]])