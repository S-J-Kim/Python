N, V, B = map(int, input().split())
adj = [[0 for i in range(N)] for j in range(N)]
visit = [False for i in range(N)]
stack = list()

def DFS(vertex):
    visit[vertex] = True
    stack.append(vertex + 1)

    for node in range(len(adj[vertex])):
        if adj[vertex][node] and not visit[node]:
            visit[node] = True
            DFS(node)

            
for i in range(V):
    S, D = map(int, input().split())
    adj[S - 1][D - 1] = adj[D - 1][S - 1] = 1

DFS(B - 1)
print(stack)
