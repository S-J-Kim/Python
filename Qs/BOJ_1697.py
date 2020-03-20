from collections import deque

N, K = map(int, input().split())
field = [0 for _ in range(100001)]
visit = [False for _ in range(100001)]
q = deque()

def bfs(n, c):
    q.append([n, c])
    visit[n] = True
    field[n] = c
   
    while q.__len__():
        u = q.popleft()
        visit[u[0]] = True
        nx = [u[0] - 1, u[0] + 1, 2 * u[0]]
        
        for i in range(3):
            nxt = nx[i]
            
            if 0 <= nxt < 100001 and not visit[nxt]:
                q.append([nxt, u[1] + 1])
                visit[nxt] = True
                field[nxt] = u[1] + 1
                if nxt == K: break


bfs(N, 0)
print(field[K])