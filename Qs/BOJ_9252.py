A = list(input())
B = list(input())

a, b = len(A), len(B)

dp = [['0' for _ in range(a)] for _ in range(b)]

for i in range(a):
    dp[0][i] = A[i] if A[i] == B[0] else dp[0][i - 1]

for i in range(1, b):
    dp[i][0] = dp[i - 1][0] if not A[0] == B[i] else B[i]
     
    for j in range(1, a):
        if A[j] == B[i]:
            dp[i][j] = dp[i - 1][j - 1] + A[j]
        else:
            dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
            
dp[b - 1][a - 1] = dp[b - 1][a - 1][1:] if dp[b - 1][a - 1][0] == '0' else dp[b - 1][a - 1]

print(len(dp[b - 1][a - 1]))
if len(dp[b - 1][a - 1]) > 0: print(dp[b - 1][a - 1])