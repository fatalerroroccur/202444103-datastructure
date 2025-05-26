class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
    def print_graph(self, n):
        for r in range(n):
            for c in range(n):
                print(self.graph[r][c], end=' ')
            print()

G1 = Graph(4)
G3 = Graph(4)
G_self = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("G1 무방향 그래프")
G1.print_graph(G1.SIZE)

# 0 == A, 1 == B, 2 == C, 3 == D
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print("G3 방향 그래프")
G3.print_graph(G3.SIZE)

# 0 == A, 1 == B, 2 == C, 3 == D
G_self.graph[0][3] = 1
G_self.graph[1][2] = 1; G_self.graph[1][3] = 1
G_self.graph[2][1] = 1
G_self.graph[3][0] = 1; G_self.graph[3][1] = 1

print("G_self 무방향 그래프")
for r in range(G_self.SIZE):
    for c in range(G_self.SIZE):
        print(G_self.graph[r][c], end=' ')
    print()


graph = [
    [0,1,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [0,1,1,0,1,1,1,0],
    [0,0,0,1,0,1,0,0],
    [0,0,0,1,1,0,0,0],
    [0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,1,0]
]
def dfs(g,i,visited):
    visited[i] = True
    print(chr(ord('A')+1),end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g,j,visited)
            visited[j]=1
def bfs(g,i,visited):
    visited[i] = True
    print(chr(ord('A') + 1), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)
            visited[j] = 1
visited_bfs = [False for _ in range(len(graph))]
visited_dfs = [False for _ in range(len(graph))]
dfs(graph,7,visited_dfs)
print()
bfs(graph,4,visited_bfs)
print()


