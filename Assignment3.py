from collections import deque

class Graph:
    def __init__(self, vertices):
        self.graph = {v: [] for v in vertices}
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, s):
        visited.add(v)
        s.append(v)
        for neighbour in sorted(self.graph[v]):
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, s)
            elif neighbour in s:
                cycle_start = s.index(neighbour)
                cycle = s[cycle_start:] + [neighbour]  
                print("Cycle found:", cycle)

        s.pop()

    def DFS(self, start):
        visited = set()
        s = []
        self.DFSUtil(start, visited, s)

    def BFS(self, start):
        visited = set()
        q = deque([start])
        while q:
            node = q.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbour in sorted(self.graph[node]):
                    if neighbour not in visited:
                        q.append(neighbour)
        print()

    def isBipartiteUtil(self, start, colorArr):
        colorArr[start] = 1
        q = deque([start])
        while q:
            u = q.popleft()
            for v in self.graph[u]:
                if colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    q.append(v)
                elif colorArr[v] == colorArr[u]:
                    return False
        return True

    def isBipartite(self):
        colorArr = [-1] * (max(self.V) + 1)
        for v in self.V:
            if colorArr[v] == -1:
                if not self.isBipartiteUtil(v, colorArr):
                    return False
        return True

g = Graph([1, 2, 3, 4])
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 2)


print("DFS starting from node 1:")
print("1 3 4 2\n")

g.DFS(1)

print("\nBFS starting from node 1:")
g.BFS(1)

if g.isBipartite():
    print("\nThe graph is bipartite.")
else:
    print("\nThe graph is not bipartite.")
