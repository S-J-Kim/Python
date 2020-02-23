import sys
import math
input=sys.stdin.readline


n = int(input())
k=int(math.sqrt(n))

dp = [[0 for _ in range(n+1)] for _ in range(2)]

for i in range(n+1):
    dp[0][i]=i


for i in range(1, k+1):
    for j in range(1, i*i):
        dp[i%2][j] = dp[(i%2)-1][j]

    for j in range(i*i, n+1):
        dp[i%2][j] = min(dp[i%2][j-(i*i)] + 1, dp[(i%2)-1][j])


print(dp[(k%2)][n])