from collections import defaultdict,deque;

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    
    def dfs_recursive(self,vertex,visited=None):
        if visited is None:
            visited=set()
        
        visited.add(vertex)
        print(vertex, end=" ")
        
        for children in self.graph[vertex]:
            if children not in visited:
                self.dfs_recursive(children,visited)
                
    def bfs_recursive(self,start):
        visited=set()
        queue=deque([start])
        visited.add(start)
        
        while queue:
            vertex=queue.popleft()
            print(vertex,end=" ")
            for children in self.graph[vertex]:
                if children not in visited:
                    queue.append(children)
                    visited.add(children)
        
    
                
                
g=Graph()

g.add_edge(1,2)
g.add_edge(3,2)
g.add_edge(4,3)

print("depth first search from starting vertex 1")
g.dfs_recursive(1)

print("\nbreadth first search from starting vertex 1")
g.bfs_recursive(1)
            