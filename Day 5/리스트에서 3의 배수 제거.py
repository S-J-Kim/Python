li = list(range(1, 51))
print(li)

li2 = list(range(3, 51, 3))

for val in li2:
    li.remove(val)

print(li)