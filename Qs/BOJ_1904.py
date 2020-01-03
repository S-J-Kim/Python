ways = [1, 1, 2]


n = int(input())

for i in range(3, n + 1):
    ways[0], ways[1] = ways[1], ways[2]
    ways[2] = (ways[1] + ways[0]) % 15746

print(ways[2])