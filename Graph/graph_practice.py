class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def insert_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edges(self,vertex,edges,bi=False):
        self.insert_vertex(vertex)
        self.insert_vertex(edges)
        self.graph[vertex].append(edges) 

        if bi:
            self.graph[edges].append(vertex)  

    def delete_vertex(self,vertex):
        for vrtx,edges in self.graph.items():
            if vertex in edges:
                self.graph[vrtx].removes(vertex)

        del self.graph[vertex]                 
    
    def Bfs (self):
        traversal = []

        for vertex in self.graph:
            if vertex not in traversal:
                queue = [vertex]

                while queue:
                    node = queue.pop(0) 
                    if node not in traversal:
                        traversal.append(node)
                        
                        for edge in self.graph.get(node,[]):
                            if edge not in traversal:
                                queue.append(edge)

        return traversal    

    def Dfs (self):
        traversal = []

        def Dfs_util(vertex):
            traversal.append(vertex)

            for edge in self.graph.get(vertex,[]):
                if edge not in traversal:
                    Dfs_util(edge)

        for vertex in self.graph:
            if vertex  not in traversal:
                Dfs_util(vertex)    

        return traversal               

                                 
       

graph = Graph()

graph.add_edges(1,2)
graph.add_edges(1,4)
graph.add_edges(2,3)
graph.add_edges(3,4)


print(graph.Bfs())
print(graph.Dfs())
