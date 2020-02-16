import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

inf = 99999999

city = [[inf for _ in range(n)] for _ in range(n)]

for i in range(m):
    src, dest, cost = map(int, input().split())
    if city[src - 1][dest - 1] > cost:
        city[src - 1][dest - 1] = cost
        
for i in range(n):
    for j in range(n):
        for k in range(n):
            if city[j][i] + city[i][k] < city[j][k]:
                city[j][k] = city[j][i] + city[i][k]
    
print(city)