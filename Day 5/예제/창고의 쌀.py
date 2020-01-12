rice = 100000
day = 0
mouse = 2

while rice > 0:
    day += 1
    
    if not(day % 10): mouse *= 2
    
    rice -= (mouse * 20)

print(f'{day}일 만에 쌀이 없어지고, 그때 쥐는 총 {mouse}마리이다.')