A = list(input())
B = list(input())

a, b = len(A), len(B)

dp = [[0 for _ in range(a)] for _ in range(b)]

for i in range(a):
    dp[0][i] = 1 if A[i] == B[0] else dp[0][i - 1]

for i in range(1, b):
    dp[i][0] = dp[i - 1][0] if not A[0] == B[i] else 1
     
    for j in range(1, a):
        if A[j] == B[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            

print(dp[b - 1][a - 1])