

N = int(input())

map_ = [list(input()) for _ in range(N)]
visit = [[False for i in range(N)] for j in range(N)]
houses = []

def DFS(i, j, c):
    visit[i][j] = True
    
    if i > 0 and not visit[i - 1][j] and map_[i - 1][j] == '1':
        c = max(c, DFS(i - 1, j, c + 1))
    
    if j < N - 1 and not visit[i][j + 1] and map_[i][j + 1] == '1':
        c = max(c, DFS(i, j + 1, c + 1))
    
    if i < N - 1 and not visit[i + 1][j] and map_[i + 1][j] == '1':
        c = max(c, DFS(i + 1, j, c + 1))
        
    if j > 0 and not visit[i][j - 1] and map_[i][j - 1] == '1':
        c = max(c, DFS(i, j - 1, c + 1))
        
    return c

for i in range(N):
    for j in range(N):
        if map_[i][j] == '1' and not visit[i][j]:
            houses.append(DFS(i, j, 1))
            

houses.sort()

print(len(houses))
for val in houses:
    print(val)
