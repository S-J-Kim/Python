n = int(input())

a = list(map(int, input().split()))

mx = 0

dp1, dp2 = [1] * n, [1] * n
dp =[]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp1[i] <= dp1[j]:
            dp1[i] = dp1[j] + 1

for i in range(n - 1, 0, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and dp2[i] <= dp2[j]:
            dp2[i] = dp2[j] + 1
            
for i in range(len(dp1)):
    dp.append(dp1[i] + dp2[i] - 1)
    
print(max(dp))