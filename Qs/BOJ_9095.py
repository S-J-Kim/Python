T = int(input())
li = [0] * 12
li[1] = 1
li[2] = 2
li[3] = 4

for i in range(4, 12):
    li[i] = li[i - 1] + li[i - 2] + li[i - 3]
    
for i in range(T):
    n = int(input())
    print(li[n])
    