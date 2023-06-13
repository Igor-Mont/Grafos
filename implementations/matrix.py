from linked_list import LinkedList

class Vertex:
  def __init__(self, data, index):
    self.data = data
    self.index = index
    self.degree = 0

class Graph:
  def __init__(self, type):
    self.graph = dict()
    self.type = type
    self.vertices = list()
    self.matrix = list()
    self.edges = list()

  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = LinkedList()
      
  def add_vertex_matrix(self, vertex):
    if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.matrix.append([0] * len(self.vertices))
            for row in self.matrix:
                row.append(0)    

  def add_edge(self, vertex1, vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      vertex1.degree += 1
      vertex2.degree += 1
      self.graph[vertex1].append(vertex2)
      self.graph[vertex2].append(vertex1)
      edge = (vertex1.data, vertex2.data)
      if tuple(reversed(edge)) not in self.edges:
        self.edges.append(edge)
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")
    
  def add_edge_matrix(self, vertex1, vertex2):
    index1 = self.vertices.index(vertex1)
    index2 = self.vertices.index(vertex2)
    self.matrix[index1][index2] = 1
    self.matrix[index2][index1] = 1

  def get_vertexes(self):
    return [vertex.data for vertex in self.graph.keys()]

  def get_adjacent_vertices(self, vertex):
    if vertex in self.graph:
      return [adjacent.data for adjacent in self.graph[vertex]]
    return list()

  def get_edges(self):
    return self.edges

  def has_edge(self, vertex1, vertex2):
    if vertex1 in self.graph and vertex2 in self.graph:
      # aqui poderia ser apenas um lado ou outro do "and", mas fiz as duas pra garantir
      return vertex2 in self.graph[vertex1] and vertex1 in self.graph[vertex2]
    return False

  def vertex_degree(self, index):
    for vertex in self.graph:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")

  def neighboring_vertices(self, index_v1, index_v2):
    vertex1 = None
    vertex2 = None
    for vertex in self.graph:
      if vertex.index == index_v1:
        vertex1 = vertex
      if vertex.index == index_v2:
        vertex2 = vertex

    return self.has_edge(vertex1, vertex2)

  def remove_edge(self, edge):
    if edge in self.edges:
      self.edges.remove(edge)
      return

    reversed_edge = tuple(reversed(edge))
    if reversed_edge in self.edges:
      self.edges.remove(reversed_edge)

  def print_graph(self):
    print("Quantidade de vértices:", len(self.get_vertexes()))
    print("Quantidade de arestas:", len(self.get_edges()))
    print("Arestas:", self.get_edges())
    for vertex in self.graph:
      print("Grau:", vertex.degree, "|", vertex.data, "->",
            [neighbor.data for neighbor in self.graph[vertex]])
  
  def print_matrix(self):
    for vertex in self.vertices:
        print(vertex.data, end=" ")
    print()
    for i in range(len(self.vertices)):
        print(self.vertices[i].data, end=" ")
        for j in range(len(self.vertices)):
            print(self.matrix[i][j], end=" ")
        print()

graph = Graph("")

vertex_a = Vertex("A", 1)
vertex_b = Vertex("B", 2)
vertex_c = Vertex("C", 3)
vertex_d = Vertex("D", 4)
vertex_e = Vertex("E", 5)

graph.add_vertex_matrix(vertex_a)
graph.add_vertex_matrix(vertex_b)
graph.add_vertex_matrix(vertex_c)
graph.add_vertex_matrix(vertex_d)
graph.add_vertex_matrix(vertex_e)

graph.add_edge_matrix(vertex_a, vertex_b)
graph.add_edge_matrix(vertex_c, vertex_d)
graph.add_edge_matrix(vertex_a, vertex_e)
graph.print_matrix()

# graph.add_vertex(vertex_a)
# graph.add_vertex(vertex_b)
# graph.add_vertex(vertex_c)
# graph.add_vertex(vertex_d)
# graph.add_vertex(vertex_e)

# graph.add_edge(vertex_a, vertex_b)
# graph.add_edge(vertex_b, vertex_c)
# graph.add_edge(vertex_b, vertex_d)
# graph.add_edge(vertex_b, vertex_e)
# graph.add_edge(vertex_c, vertex_c)
# graph.add_edge(vertex_c, vertex_d)
# graph.add_edge(vertex_d, vertex_e)
# graph.add_edge(vertex_e, vertex_b)

# graph.print_graph()

# graph2 = Graph("")

# vertex_a = Vertex("A", 1)
# vertex_b = Vertex("B", 2)
# vertex_c = Vertex("C", 3)
# vertex_d = Vertex("D", 4)
# vertex_e = Vertex("E", 5)

# graph2.add_vertex(vertex_a)
# graph2.add_vertex(vertex_b)
# graph2.add_vertex(vertex_c)
# graph2.add_vertex(vertex_d)
# graph2.add_vertex(vertex_e)

# graph2.add_edge(vertex_a, vertex_b)
# graph2.add_edge(vertex_a, vertex_e)
# graph2.add_edge(vertex_a, vertex_d)
# graph2.add_edge(vertex_a, vertex_c)
# graph2.add_edge(vertex_b, vertex_c)
# graph2.add_edge(vertex_b, vertex_d)
# graph2.add_edge(vertex_b, vertex_e)
# graph2.add_edge(vertex_c, vertex_e)
# graph2.add_edge(vertex_c, vertex_d)
# graph2.add_edge(vertex_d, vertex_e)

# graph2.print_graph()