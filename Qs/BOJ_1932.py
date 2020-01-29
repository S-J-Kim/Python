tc = int(input())

li = []

for i in range(tc): 
    num = list(map(int, input().split()))
    li.append(num)

dp = li

for i in range(1, tc):
    dp[i][0] = dp[i - 1][0] + li[i][0]
    for j in range(1, i):
        dp[i][j] = li[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
    dp[i][-1] = dp[i - 1][-1] + li[i][-1]
    
print(max(dp[tc - 1]))