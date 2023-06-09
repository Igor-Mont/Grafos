from linked_list import LinkedList

class Vertex:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.adjacent = LinkedList()

    def add_adjacent(self, vertex):
        self.adjacent.append(vertex)
    
    def remove_adjacent(self, vertex):
        self.adjacent.remove(vertex)
        

    def print_adjacent(self):
        print(f"Vertex {self.index} - Value: {self.value}")
        print("adjacent:")
        for vertex in self.adjacent:
            print("-> {}".format(vertex.index), end=" ")
        print("\n")


class Graphs:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, index, value):
        vertex = Vertex(index, value)
        self.vertices[index] = vertex

    def add_edge(self, origin, destiny):
        if origin in self.vertices and destiny in self.vertices:
            vertex_origin = self.vertices[origin]
            vertex_destiny = self.vertices[destiny]
            vertex_origin.add_adjacent(vertex_destiny)
            vertex_destiny.add_adjacent(vertex_origin)
            
    def remove_edge(self, origin, removed):
        if origin in self.vertices and removed in self.vertices:
            vertex_origin = self.vertices[origin]
            vertex_removed = self.vertices[removed]
            vertex_origin.remove_adjacent(vertex_removed)
            vertex_removed.remove_adjacent(vertex_origin)

    def imprimir_graphs(self):
        for vertex in self.vertices.values():
            vertex.print_adjacent()

# Exemplo de uso
graphs = Graphs()

# Adicionando vértices
graphs.add_vertex(0, 'A')
graphs.add_vertex(1, 'B')
graphs.add_vertex(2, 'C')
graphs.add_vertex(3, 'D')
graphs.add_vertex(5, 'E')
graphs.add_vertex(6, 'F')
graphs.add_vertex(7, 'G')
graphs.add_vertex(8, 'H')

# Adicionando arestas
graphs.add_edge(0, 1)
graphs.add_edge(0, 8)
graphs.add_edge(0, 2)
graphs.add_edge(6, 2)
graphs.add_edge(1, 3)
graphs.add_edge(1, 7)
graphs.add_edge(8, 3)
graphs.add_edge(5, 3)
graphs.add_edge(5, 8)
graphs.remove_edge(5, 3)
graphs.remove_edge(1, 3)
graphs.remove_edge(0, 1)

# Imprimindo o graphs
graphs.imprimir_graphs()
