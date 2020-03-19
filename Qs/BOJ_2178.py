import queue

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
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
        
        if X > 0 and maze[Y][X - 1] == '1' and not visit[Y][X - 1]:
            q.put([X - 1, Y, C + 1])
            visit[Y][X - 1] = True
            cost[Y][X - 1] = C + 1
        
        if X < M - 1 and maze[Y][X + 1] == '1' and not visit[Y][X + 1]:
            q.put([X + 1, Y, C + 1])
            visit[Y][X + 1] = True
            cost[Y][X + 1] = C + 1
            
        if Y > 0 and maze[Y - 1][X] == '1' and not visit[Y - 1][X]:
            q.put([X, Y - 1, C + 1])
            visit[Y - 1][X] = True
            cost[Y - 1][X] = C + 1
            
        if Y < N - 1 and maze[Y + 1][X] == '1' and not visit[Y + 1][X]:
            q.put([X, Y + 1, C + 1])
            visit[Y + 1][X] = True 
            cost[Y + 1][X] = C + 1
    
bfs(0, 0, 1)
print(cost[N - 1][M - 1])
