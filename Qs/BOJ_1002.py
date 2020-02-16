import math

tc = int(input())
point = 0


for i in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    if x1 == x2 and y1 == y2 and r1 == r2: point = -1
    elif r1 + r2 < d or abs(r1 - r2) > d: point = 0
    elif r1 + r2 == d or abs(r1 - r2) == d: point = 1
    elif abs(r1 - r2) < d < r1 + r2: point = 2
    
    print(point)

    