import math

tc = int(input())
point = 0


for i in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))

    if abs(r1 - r2) < d < (r1 + r2): point = 2
    elif r1 + r2 == int(d) or abs(r1 - r2) == int(d): point = 1
    elif r1 + r2 < int(d) or int(d) < abs(r1 - r2) or d == 0:
        if x1 == x2 and y1 == y2:
            
    
    