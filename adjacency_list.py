'''Create the class to represent a graph as the adjacency list'''

class Graph:
    def __init__(self , num_nodes , edges):
        self.num_nodes = num_nodes
        self.edges = edges
        self.data = [[] for _ in range(num_nodes)]
    def display(self):
        for n1 , n2 in self.edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def report(self):
        return [f'{n} : {neighbour}' for n , neighbour in enumerate(self.data)]


edges = [(0,1),(0,4) , (1,2) , (1,3), (1,4) , (2,3) , (3,4)]

graph = Graph(5 , edges)
graph.display()

print(graph.data)
print(graph.report())