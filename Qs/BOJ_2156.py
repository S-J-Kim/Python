n = int(input())

w = [0] + [int(input()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

if n == 1: dp[1] = w[1]
elif n == 2: dp[2] = w[1] + w[2]
else:
    dp[1] = w[1]
    dp[2] = w[2] + w[1]
    
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i])
        

print(max(dp))