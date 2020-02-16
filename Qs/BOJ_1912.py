n = int(input())

li = list(map(int, input().split()))

tmpsum = 0
maxval = 0

dp = [-9999 for i in range(n)]
dp[0] = li[0]

for i in range(1, n):
    dp[i] = dp[i - 1] + li[i] if li[i] < dp[i - 1] + li[i] else li[i]
    
print(max(dp))