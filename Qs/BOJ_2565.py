N = int(input())

B = [-9999 for _ in range(500)]
C = []

for i in range(N):
    a, b = map(int, input().split())
    B[a - 1] = b

for i in range(500):
    if B[i] >= 0:
        C.append(B[i])

l = len(C)
dp = [1 for _ in range(l)]

for i in range(l):
    for j in range(i):
        if C[j] < C[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(l - max(dp))