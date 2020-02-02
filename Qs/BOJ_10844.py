n = int(input())

li = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

for i in range(1, 100):
    dp = [0 for i in range(10)]
    dp[0] = li[i - 1][1]
    for j in range(1, 9):
        dp[j] = li[i - 1][j - 1] + li[i - 1][j + 1]
    dp[9] = li[i - 1][8]
    
    li.append(dp)

print(sum(li[n - 1]) % 1000000000)