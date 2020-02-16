import sys
input=sys.stdin.readline

N, K = map(int, input().split())

V = [0 for i in range(N)]
W = [0 for i in range(N)]

dp = [[0 for x in range(K + 1)] for u in range(N + 1)]

for i in range(N):
    W[i], V[i] = map(int, input().split())

for i in range(1, N + 1):
    for j in range(K + 1):
        dp[i][j] = dp[i - 1][j]
        
        if j - W[i-1] >= 0:
            dp[i][j] = max(dp[i - 1][j - W[i - 1]] + V[i - 1], dp[i - 1][j])
            
print(dp[N][K])