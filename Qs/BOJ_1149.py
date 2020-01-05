n = int(input())

li = []

for i in range(n):
    a = list(map(int, input().split()))
    li.append(a)

dp = [[0 for _ in range(3)] for _ in range(len(li))]

dp[0][0] = li[0][0]
dp[0][1] = li[0][1]
dp[0][2] = li[0][2]

for j in range(1, len(li)):
    for i in range(3):
        dp[j][i] = min(dp[j - 1][i - 1] + li[j][i], dp[j - 1][(i + 1) % 3] + li[j][i])
        
print(min(dp[len(li) - 1]))