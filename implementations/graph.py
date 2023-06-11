from linked_list import LinkedList

class Vertex:
  def __init__(self, data):
    self.data = data

class Graph:
  def __init__(self):
    self.graph = dict()

  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = LinkedList()

  def add_edge(self, vertex1, vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      self.graph[vertex1].append(vertex2)
      self.graph[vertex2].append(vertex1)
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")

  def get_vertexes(self):
    return [vertex.data for vertex in self.graph.keys()]
  
  def get_adjacent_vertices(self, vertex):
    if vertex in self.graph:
        return [adjacent.data for adjacent in self.graph[vertex]]
    return list()

  def get_edges(self):
    edges = list()
    for vertex in self.graph:
      for neighbor in self.graph[vertex]:
        edge = (vertex.data, neighbor.data)
        # esse if é pra tirar as duplicatas, pois é um grafo não direcionado
        # ("A", "B") == ("B", "A")
        if tuple(reversed(edge)) not in edges:
          edges.append(edge)
    return edges

  def has_edge(self, vertex1, vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      # aqui poderia ser apenas um lado ou outro do "and", mas fiz as duas pra garantir
      return vertex2 in self.graph[vertex1] and vertex1 in self.graph[vertex2]
    return False

  def print_graph(self):
    for vertex in self.graph:
      print(vertex.data, "->", [neighbor.data for neighbor in self.graph[vertex]])

# Inicializar 
graph = Graph()

# Criar vértices
vertex_a = Vertex("A")
vertex_b = Vertex("B")
vertex_c = Vertex("C")
vertex_d = Vertex("D")

# Adicionar vértices
graph.add_vertex(vertex_a)
graph.add_vertex(vertex_b)
graph.add_vertex(vertex_c)
graph.add_vertex(vertex_d)

# Adicionar arestas
graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_b, vertex_c)
graph.add_edge(vertex_c, vertex_a)
graph.add_edge(vertex_d, vertex_a)

# Obtendo vértices e arestas
vertexes = graph.get_vertexes()
edges = graph.get_edges()
print(vertexes)
print(edges)
print(graph.get_adjacent_vertices(vertex_a))
print(graph.get_adjacent_vertices(vertex_b))
print(graph.get_adjacent_vertices(vertex_c))
print(graph.get_adjacent_vertices(vertex_d))

# Verificando a existência de uma aresta
has_edge = graph.has_edge(vertex_b, vertex_b)
print(has_edge)

# Imprimindo o grafo
graph.print_graph()
