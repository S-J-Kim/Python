from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())
farm = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[False for _ in range(M)] for __ in range(N)] for ___ in range(H)]
q = deque()

def bfs():
    dx = [0, 0, 1, 0, -1, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [-1, 0, 0, 0, 0, 1]

    while q.__len__():
        n = q.popleft()
        visit[n[2]][n[1]][n[0]] = True
    
        for i in range(6):
            nx = n[0] + dx[i]
            ny = n[1] + dy[i]
            nz = n[2] + dz[i]
        
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and not visit[nz][ny][nx] and farm[nz][ny][nx] >= 0:
                q.append([nx, ny, nz, n[3] + 1])
                visit[nz][ny][nx] = True
                farm[nz][ny][nx] = n[3] + 1
        

def sol():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if farm[i][j][k] == 1:
                    q.append([k, j, i, 0])
    
    bfs()
    tmp = -10
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                tmp = farm[i][j][k] if farm[i][j][k] > tmp else tmp
                if farm[i][j][k] == 0: return -1
    
    return tmp if tmp > 1 else 0
    
print(sol())