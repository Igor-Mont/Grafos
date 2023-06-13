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


class Graph:
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

  def imprimir_graph(self):
    for vertex in self.vertices.values():
      vertex.print_adjacent()

# Exemplo de uso
graph = Graph()

# Adicionando vértices
graph.add_vertex(0, 'A')
graph.add_vertex(1, 'B')
graph.add_vertex(2, 'C')
graph.add_vertex(3, 'D')
graph.add_vertex(5, 'E')
graph.add_vertex(6, 'F')
graph.add_vertex(7, 'G')
graph.add_vertex(8, 'H')

# Adicionando arestas
graph.add_edge(0, 1)
graph.add_edge(0, 8)
graph.add_edge(0, 2)
graph.add_edge(6, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 7)
graph.add_edge(8, 3)
graph.add_edge(5, 3)
graph.add_edge(5, 8)
graph.remove_edge(5, 3)
graph.remove_edge(1, 3)
graph.remove_edge(0, 1)

# Imprimindo o graph
graph.imprimir_graph()
