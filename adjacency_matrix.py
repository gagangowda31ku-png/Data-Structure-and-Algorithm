'''Create the class to represent a graph as the adjacency matrix'''

class Graph:
    def __init__(self , num_nodes , edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.matrix = [[0]* num_nodes for _ in range(num_nodes)]

    def compute(self):
        for v , u in self.edges:
            self.matrix[v][u] = 1
            self.matrix[u][v] = 1
    def display(self):
        for row in self.matrix:
            print(row)

edges = [(0,1),(0,4) , (1,2) , (1,3), (1,4) , (2,3) , (3,4)]
graph = Graph(5 , edges)
graph.compute()
graph.display()

