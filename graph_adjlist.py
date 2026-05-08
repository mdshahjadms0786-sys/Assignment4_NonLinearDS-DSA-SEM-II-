# Graph using adjacency list + BFS + DFS

from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

    def bfs(self, start):
        visited = set()
        q = deque([start])
        order = []
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neigh in self.adj.get(node, []):
                    q.append(neigh)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        def dfs_util(node):
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neigh in self.adj.get(node, []):
                    dfs_util(neigh)
        dfs_util(start)
        return order

if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")

    print("Adjacency List:", g.adj)
    print("BFS from A:", g.bfs("A"))
    print("DFS from A:", g.dfs("A"))


# Adjacency List: {'A': ['B', 'C'], 'B': ['D'], 'C': ['E']}
# BFS from A: ['A', 'B', 'C', 'D', 'E']
# DFS from A: ['A', 'B', 'D', 'C', 'E']
