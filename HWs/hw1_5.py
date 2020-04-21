number_of_lecture = int(input())
lectures = [list(map(int, input().split())) for _ in range(number_of_lecture)]

lectures = sorted(lectures, key=lambda x: x[2])

res = [lectures[0]]
output = []

for i in range(1, number_of_lecture):
    if lectures[i][1] >= res[-1][2]: res.append(lectures[i])

for i in res:
    output.append(i[0])

print(output)