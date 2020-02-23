N = int(input())

li = [0 for _ in range(31)]

li[2] = 3

for i in range(4, 31, 2):
    li[i] += (3 * li[i - 2])
    
    for j in range(2, i - 2, 2):
        li[i] += (2 * li[j])

    li[i] += 2

print(li[N])

        