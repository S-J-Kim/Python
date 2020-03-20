from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for __ in range(N)]
q = deque()

def bfs():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    while q.__len__():
        n = q.popleft()
        visit[n[1]][n[0]] = True
    
        for i in range(4):
            nx = n[0] + dx[i]
            ny = n[1] + dy[i]
        
            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx] and farm[ny][nx] >= 0:
                q.append([nx, ny, n[2] + 1])
                visit[ny][nx] = True
                farm[ny][nx] = n[2] + 1
        

def sol():
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                q.append([j, i, 0])
    
    bfs()
    tmp = -10
    isZero = False
    
    for i in range(N):
        for j in range(M):
            tmp = farm[i][j] if farm[i][j] > tmp else tmp
            if farm[i][j] == 0: return -1
    
    return tmp if tmp > 1 else 0
    
print(sol())