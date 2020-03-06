import queue

N, V, B = map(int, input().split())
adj = [[0 for i in range(N)] for j in range(N)]
visit = [False for i in range(N)]
q = queue.Queue()
l = list()



def BFS(vertex):
    q.put(vertex)
    visit[vertex] = True
    
    while q.qsize():
        next_node = q.get()
        #print(f'visited node : {next_node+1}')
        l.append(next_node + 1)
        for i in range(len(adj[next_node])):
            if adj[next_node][i] and not visit[i]:
                q.put(i)
                visit[i] = True
                
for i in range(V):
    S, D = map(int, input().split())
    adj[S - 1][D - 1] = adj[D - 1][S - 1] = 1

BFS(B - 1)
print(l)

        
