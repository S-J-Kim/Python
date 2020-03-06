import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

def DFS(i, j, c, map_, visit, M, N):
    visit[i][j] = True
    
    if i > 0 and not visit[i - 1][j] and map_[i - 1][j]:
        c = max(c, DFS(i - 1, j, c + 1, map_, visit, M, N))
    
    if j < M - 1 and not visit[i][j + 1] and map_[i][j + 1]:
        c = max(c, DFS(i, j + 1, c + 1, map_, visit, M, N))
    
    if i < N - 1 and not visit[i + 1][j] and map_[i + 1][j]:
        c = max(c, DFS(i + 1, j, c + 1, map_, visit, M, N))
        
    if j > 0 and not visit[i][j - 1] and map_[i][j - 1]:
        c = max(c, DFS(i, j - 1, c + 1, map_, visit, M, N))
        
    return c

def Solve(M, N, K):
    
    field = [[False for i in range(M)] for j in range(N)]
    visited = [[False for i in range(M)] for j in range(N)]
    
    for i in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = True

    A = []

    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                A.append(DFS(i, j, 1, field, visited, M, N))
        
    return len(A)

for i in range(T):
    M, N, K = map(int, input().split())
    print(Solve(M, N, K))