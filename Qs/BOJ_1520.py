import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())

map_ = [list(map(int, input().split())) for _ in range(m)]
stuck = [[True for _ in range(n)] for _ in range(m)]
count = 0


def CountRoute(x, y):
    global count

    if x == m - 1 and y == n - 1:
        count += 1
        return
    
    if x < m - 1 and map_[x + 1][y] < map_[x][y] and stuck[x + 1][y]:
        CountRoute(x + 1, y)
    
    if y < n - 1 and map_[x][y + 1] < map_[x][y] and stuck[x][y + 1]:
        CountRoute(x, y + 1)
        
    if x != 0 and map_[x - 1][y] < map_[x][y] and stuck[x - 1][y]:
        CountRoute(x - 1, y)
        
    if y != 0 and map_[x][y - 1] < map_[x][y] and stuck[x][y - 1]:
        CountRoute(x, y - 1)

    else:
        stuck[x][y] = False

CountRoute(0, 0)
print(count)
