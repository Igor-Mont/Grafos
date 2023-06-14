from linked_list import LinkedList

class Vertex:
  def __init__(self, data, index):
    self.data = data
    self.index = index
    self.degree = 0

class Graph:
  def __init__(self, type):
    self.type = type
    self.adjacency_list = dict()
    self.edges = list()
    self.vertices = list()
    self.matrix = list()
    self.edges_matrix = list()
    self.edge_count = 0

  def add_vertex_list(self, vertex):
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = LinkedList()
      
  def add_vertex_matrix(self, vertex):
    if vertex not in self.vertices:
      self.vertices.append(vertex)
      self.matrix.append([0] * len(self.vertices))
      for row in self.matrix[:-1]:
        row.append(0)

  def add_edge_list(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      vertex1.degree += 1
      vertex2.degree += 1
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)
      edge = (vertex1.data, vertex2.data)
      if tuple(reversed(edge)) not in self.edges:
        self.edges.append(edge)
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")
    
  def add_edge_matrix(self, vertex1, vertex2):
    if vertex1 in self.vertices and vertex2 in self.vertices:
      index1 = self.vertices.index(vertex1)
      index2 = self.vertices.index(vertex2)
      vertex1.degree += 1
      vertex2.degree += 1
      self.matrix[index1][index2] += 1
      self.matrix[index2][index1] += 1
      edge = (vertex1.data, vertex2.data)
      self.edges_matrix.append(edge)
      self.edge_count += 1
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")

  def get_vertexes_list(self):
    return [vertex.data for vertex in self.adjacency_list.keys()]
  
  def get_vertexes_matrix(self):
    return [vertex.data for vertex in self.vertices]

  def get_edges_list(self):
    return self.edges
  
  def get_edges_matrix(self, filtered=False):
    filtered_edges = []
    if filtered:
      for edge in self.edges_matrix:
        sorted_edge = tuple(sorted(edge))
        if sorted_edge not in filtered_edges:
          filtered_edges.append(edge)
      return filtered_edges
    return self.edges_matrix

  def has_edge_list(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      # aqui poderia ser apenas um lado ou outro do "and", mas fiz as duas pra garantir
      return vertex2 in self.adjacency_list[vertex1] and vertex1 in self.adjacency_list[vertex2]
    return False
  
  def has_edge_matrix(self, vertex1, vertex2):
    if(self.vertices[0].index == 0):
      return self.matrix[vertex1.index][vertex2.index] >= 1
      
    return self.matrix[vertex1.index-1][vertex2.index-1] >= 1
  
  def neighboring_vertices_matrix(self, index_v1, index_v2):
    vertex1 = None
    vertex2 = None
    for vertex in self.vertices:
      if vertex.index == index_v1:
        vertex1 = vertex
      if vertex.index == index_v2:
        vertex2 = vertex

    return self.has_edge_matrix(vertex1, vertex2)
     
  def vertex_degree_list(self, index):
    for vertex in self.adjacency_list:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")
  
  def vertex_degree_matrix(self, index):
    for vertex in self.vertices:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")

  def neighboring_vertices_list(self, index_v1, index_v2):
    vertex1 = None
    vertex2 = None
    for vertex in self.adjacency_list:
      if vertex.index == index_v1:
        vertex1 = vertex
      if vertex.index == index_v2:
        vertex2 = vertex

    return self.has_edge(vertex1, vertex2)

  def remove_edge_list(self, edge):
    if edge in self.edges:
      self.edges.remove(edge)
      return

    reversed_edge = tuple(reversed(edge))
    if reversed_edge in self.edges:
      self.edges.remove(reversed_edge)
      
  def remove_edge_matrix(self, vertex1, vertex2):
    if vertex1 in self.vertices and vertex2 in self.vertices:
      if self.has_edge_matrix(vertex1, vertex2):
        index1 = self.vertices.index(vertex1)
        index2 = self.vertices.index(vertex2)
        vertex1.degree -= 1
        vertex2.degree -= 1
        self.matrix[index1][index2] -= 1
        self.matrix[index2][index1] -= 1
        edge = (vertex1.data, vertex2.data)
        if edge in self.edges:
          self.edges.remove(edge)
      else:
        raise ValueError("Edge does not exist in the graph.")
    else:
      raise ValueError("One or both vertices do not exist in the graph.")


  def print_list(self):
    print("Quantidade de vértices:", len(self.get_vertexes_list()))
    print("Quantidade de arestas:", len(self.get_edges_list()))
    print("Arestas:", self.get_edges_list())
    for vertex in self.adjacency_list:
      print("Grau:", vertex.degree, "|", vertex.data, "->",
            [neighbor.data for neighbor in self.adjacency_list[vertex]])
  
  def print_matrix(self):
    print("Quantidade de vertices:", len(self.get_vertexes_matrix()))
    print("Quantidade de arestas:", self.edge_count)
    print("Arestas:", self.get_edges_matrix())
    print("  ", end="")
    for vertex in self.vertices:
        print(vertex.data, end=" ")
    print()
    for i in range(len(self.vertices)):
        print(self.vertices[i].data, end=" ")
        for j in range(len(self.vertices)):
            print(self.matrix[i][j], end=" ")
        print()

graph = Graph("matrix")
graph_2 = Graph("matrix")

vertex_a = Vertex("A", 0)
vertex_b = Vertex("B", 1)
# vertex_c = Vertex("C", 2)
# vertex_d = Vertex("D", 3)
# vertex_e = Vertex("E", 4)

# graph.add_vertex_matrix(vertex_a)
# graph.add_vertex_matrix(vertex_b)

graph_2.add_vertex_list(vertex_a)
graph_2.add_vertex_list(vertex_b)
# graph.add_vertex_matrix(vertex_c)
# graph.add_vertex_matrix(vertex_d)
# graph.add_vertex_matrix(vertex_e)

graph_2.add_edge_list(vertex_a, vertex_b)
# graph.add_edge_matrix(vertex_a, vertex_a)
# graph.add_edge_matrix(vertex_b, vertex_a)
# graph.add_edge_matrix(vertex_c, vertex_d)
# graph.add_edge_matrix(vertex_a, vertex_e)

# graph.remove_edge_matrix(vertex_a, vertex_a)

# print(graph.has_edge_matrix(vertex_a, vertex_a))
# print(graph.has_edge_matrix(vertex_a, vertex_b))

# print(graph.has_edge_matrix(vertex_c, vertex_d))

# print(graph.neighboring_vertices_matrix(1, 2))

graph_2.print_list()

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