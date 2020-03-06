N = int(input())
V = int(input())
count = 0
adj = [[0 for i in range(N)] for j in range(N)]
visit = [False for i in range(N)]

def DFS(vertex):
    global count
    visit[vertex] = True
    count += 1

    for node in range(len(adj[vertex])):
        if adj[vertex][node] and not visit[node]:
            visit[node] = True
            DFS(node)

            
for i in range(V):
    S, D = map(int, input().split())
    adj[S - 1][D - 1] = adj[D - 1][S - 1] = 1

DFS(0)  
print(count - 1)