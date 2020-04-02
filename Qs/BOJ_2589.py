from collections import deque
import sys

input=sys.stdin.readline

L, W = map(int, input().split())
adj = [list(input()) for _ in range(L)]
li = []
cost = [[0 for _ in range(W)] for _ in range(L)]
visit = [[False for _ in range(W)] for _ in range(L)]
q = deque()
res = []

for i in range(L):
    for j in range(W):
        if adj[i][j] == 'L':
            li.append([j, i])

def bfs(x, y, c):
    for i in range(L):
        for j in range(W):
            cost[i][j] = 0
            visit[i][j] = False

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    q.append([x, y, c])
    visit[y][x] = True


    while q.__len__():
        n = q.popleft()
        
        for i in range(4):
            nx = n[0] + dx[i]
            ny = n[1] + dy[i]
            
            if 0 <= nx < W and 0 <= ny < L and adj[ny][nx] == 'L' and cost[ny][nx] == 0 and not visit[ny][nx]:
                q.append([nx, ny, n[2] + 1])
                cost[ny][nx] = n[2] + 1
                visit[ny][nx] = True

    

for i in range(len(li)):
    bfs(li[i][0], li[i][1], 0)
    for j in range(len(li)):
        if not cost[li[j][1]][li[j][0]] == 0: res.append(cost[li[j][1]][li[j][0]])

print(max(res))
    
    


        





