class Graph(object):
    def add_edge(self, edge, vertex):
        if edge in self.graph:
            self.graph[edge].append(vertex)
        else:
            self.graph[edge] = [vertex]

    def __init__(self, vertices):
        self.vertices = vertices

        self.graph = {}

    def __len__(self):
        return len(self.graph)
