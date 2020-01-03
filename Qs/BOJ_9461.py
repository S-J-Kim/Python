li = [1, 1, 1, 2, 2]

for i in range(5, 101):
    li.append(li[i - 1] + li[i - 5])

tc = int(input())

for i in range(0, tc):
    n = int(input())
    print(li[n-1])

