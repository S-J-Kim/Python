import queue

N, V, B = map(int, input().split())
adj = [[0 for i in range(N)] for j in range(N)]
visit_DFS = [False for i in range(N)]
visit_BFS = [False for i in range(N)]
dfs_seq = list()
bfs_seq = list()
q = queue.Queue()

def DFS(vertex):
    visit_DFS[vertex] = True
    dfs_seq.append(vertex + 1)

    for node in range(len(adj[vertex])):
        if adj[vertex][node] and not visit_DFS[node]:
            visit_DFS[node] = True
            DFS(node)

def BFS(vertex):
    q.put(vertex)
    visit_BFS[vertex] = True
    
    while q.qsize():
        next_node = q.get()
        bfs_seq.append(next_node + 1)
        for i in range(len(adj[next_node])):
            if adj[next_node][i] and not visit_BFS[i]:
                q.put(i)
                visit_BFS[i] = True
                
for i in range(V):
    S, D = map(int, input().split())
    adj[S - 1][D - 1] = adj[D - 1][S - 1] = 1

DFS(B - 1)
BFS(B - 1)

for val in dfs_seq:
    print(val, end=' ')
print()
for val in bfs_seq:
    print(val, end=' ')