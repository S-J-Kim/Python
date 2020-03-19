import queue
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for __ in range(N)]
cost = [[0 for _ in range(M)] for __ in range(N)]
q = queue.Queue()

def bfs(x, y, c):
    q.put([x, y, c])
    visit[y][x] = True
    cost[y][x] = c

    while q.qsize():
        next_node = q.get()
        X = next_node[0]
        Y = next_node[1]
        C = next_node[2]
        
        if X > 0 and farm[Y][X - 1] == 0 and not visit[Y][X - 1]:
            q.put([X - 1, Y, C + 1])
            visit[Y][X - 1] = True
            cost[Y][X - 1] = C + 1
        
        if X < M - 1 and farm[Y][X + 1] == 0 and not visit[Y][X + 1]:
            q.put([X + 1, Y, C + 1])
            visit[Y][X + 1] = True
            cost[Y][X + 1] = C + 1
            
        if Y > 0 and farm[Y - 1][X] == 0 and not visit[Y - 1][X]:
            q.put([X, Y - 1, C + 1])
            visit[Y - 1][X] = True
            cost[Y - 1][X] = C + 1
            
        if Y < N - 1 and farm[Y + 1][X] == 0 and not visit[Y + 1][X]:
            q.put([X, Y + 1, C + 1])
            visit[Y + 1][X] = True 
            cost[Y + 1][X] = C + 1

res = 0
cnt = 0

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            q.put([j, i, 1])
            cost[i][j] = 1
            cnt += 1

        elif farm[i][j] == -1:
            cost[i][j] = -1

if cnt == 0: res = -1
if cnt == M * N: res = 0

else:
    tmp = q.get()
    bfs(tmp[0], tmp[1], tmp[2])
    sol = -2
    for i in range(N):
        for j in range(M):
            sol = cost[i][j] if cost[i][j] > sol else sol
    
    res = sol - 1

    for i in range(N):
        for j in range(M):
            if cost[i][j] == 0: res = -1

    


print(res)