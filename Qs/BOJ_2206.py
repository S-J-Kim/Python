from collections import deque
import sys

sys = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visit = [[[False for _ in range(M)] for __ in range(N)] for ___ in range(2)]
cost = [[[0 for _ in range(M)] for __ in range(N)] for ___ in range(2)]
q = deque()

def bfs(x, y, c, broke):
    q.append([x, y, c, broke])
    visit[0][y][x] = True
    cost[0][y][x] = c
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while q.__len__():
        n = q.popleft()
        if n[3]: visit[1][n[1]][n[0]] = True
        else: visit[0][n[1]][n[0]] = True
        
        for i in range(4):
            nx = n[0] + dx[i]
            ny = n[1] + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if not n[3]:
                    if not visit[0][ny][nx]:
                        if maze[ny][nx] == '0':
                            q.append([nx, ny, n[2] + 1, n[3]])
                            visit[0][ny][nx] = True
                            cost[0][ny][nx] = n[2] + 1 
                        
                        else:
                            q.append([nx, ny, n[2] + 1, True])
                            visit[1][ny][nx] = True
                            cost[1][ny][nx] = n[2] + 1 

                        
                else:
                    if not visit[1][ny][nx]:
                        if maze[ny][nx] == '0':
                            q.append([nx, ny, n[2] + 1, n[3]])
                            visit[1][ny][nx] = True
                            cost[1][ny][nx] = n[2] + 1
                                                   
bfs(0, 0, 1, False)

if not visit[0][N - 1][M - 1]: cost[0][N - 1][M - 1] = -1
if not visit[1][N - 1][M - 1]: cost[1][N - 1][M - 1] = -1
