from linked_list import LinkedList

class Vertex:
  def __init__(self, data, index):
    self.data = data
    self.index = index
    self.degree = 0

class Graph:
  def __init__(self, representation_type):
    self.representation_type = representation_type
    self._edge_count = 0
    self.is_representation_list = representation_type == "list"
    if not self.is_representation_list:
      self.matrix = list()
      self.edges_matrix = list()
      self.vertices = list()
      return
    elif self.is_representation_list:
      self.adjacency_list = dict()
      self.edges = list()
    else:
      raise ValueError("Invalid representation type. Only 'matrix' or 'list' representation is supported.")

  def add_vertex(self, vertex):
    if self.is_representation_list:
      self._add_vertex_list(vertex)
    else:
      self._add_vertex_matrix(vertex)
    
  def _add_vertex_list(self, vertex):
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = LinkedList()
      
  def _add_vertex_matrix(self, vertex):
    if vertex not in self.vertices:
      self.vertices.append(vertex)
      self.matrix.append([0] * len(self.vertices))
      for row in self.matrix[:-1]:
        row.append(0)

  def get_edge_count(self):
    return self._edge_count

  def add_edge(self, vertex1, vertex2):
    if self.is_representation_list:
      self._add_edge_list(vertex1, vertex2)
    else:
      self._add_vertex_matrix(vertex1, vertex2)

  def _add_edge_list(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      vertex1.degree += 1
      vertex2.degree += 1
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)
      edge = (vertex1.data, vertex2.data)
      self.edges.append(edge)
      self._edge_count += 1
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")
    
  def _add_edge_matrix(self, vertex1, vertex2):
    if vertex1 in self.vertices and vertex2 in self.vertices:
      index1 = self.vertices.index(vertex1)
      index2 = self.vertices.index(vertex2)
      vertex1.degree += 1
      vertex2.degree += 1
      self.matrix[index1][index2] += 1
      self.matrix[index2][index1] += 1
      edge = (vertex1.data, vertex2.data)
      self.edges_matrix.append(edge)
      self._edge_count += 1
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")

  def get_vertices(self):
    if self.is_representation_list:
      return self._get_vertices_list()
    else:
      return self._get_vertices_matrix()
  
  def _get_vertices_list(self):
    return [vertex.data for vertex in self.adjacency_list.keys()]
  
  def _get_vertices_matrix(self):
    return [vertex.data for vertex in self.vertices]

  def get_edges(self, filtered=False):
    if self.is_representation_list:
      return self._get_edges_list(filtered)
    else:
      return self._get_edges_matrix(filtered)
    
  def _get_edges_list(self,  filtered=False):
    filtered_edges = []
    if filtered:
      for edge in self.edges:
        sorted_edge = tuple(sorted(edge))
        if sorted_edge not in filtered_edges:
          filtered_edges.append(edge)
      return filtered_edges
    return self.edges
  
  def _get_edges_matrix(self, filtered=False):
    filtered_edges = []
    if filtered:
      for edge in self.edges_matrix:
        sorted_edge = tuple(sorted(edge))
        if sorted_edge not in filtered_edges:
          filtered_edges.append(edge)
      return filtered_edges
    return self.edges_matrix

  def has_edge(self, vertex1, vertex2):
    if self.is_representation_list:
      return self._has_edge_list(vertex1, vertex2)
    else:
      return self._has_edge_matrix(vertex1, vertex2)

  def _has_edge_list(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      return vertex2 in self.adjacency_list[vertex1] and vertex1 in self.adjacency_list[vertex2]
    return False
  
  def _has_edge_matrix(self, vertex1, vertex2):
    if(self.vertices[0].index == 0):
      return self.matrix[vertex1.index][vertex2.index] >= 1
      
    return self.matrix[vertex1.index-1][vertex2.index-1] >= 1

  def has_edge(self, vertex1, vertex2):
    if self.is_representation_list:
      return self._neighboring_vertices_list(vertex1, vertex2)
    else:
      return self._neighboring_vertices_matrix(vertex1, vertex2)
    
  def _neighboring_vertices_list(self, index_v1, index_v2):
    vertex1 = None
    vertex2 = None
    for vertex in self.adjacency_list:
      if vertex.index == index_v1:
        vertex1 = vertex
      if vertex.index == index_v2:
        vertex2 = vertex

    return self.has_edge(vertex1, vertex2)

  def _neighboring_vertices_matrix(self, index_v1, index_v2):
    vertex1 = None
    vertex2 = None
    for vertex in self.vertices:
      if vertex.index == index_v1:
        vertex1 = vertex
      if vertex.index == index_v2:
        vertex2 = vertex

    return self.has_edge(vertex1, vertex2)
  
  def vertex_degree(self, index):
    if self.is_representation_list:
      return self._vertex_degree_list(index)
    else:
      return self._vertex_degree_matrix(index)
    
  def _vertex_degree_list(self, index):
    for vertex in self.adjacency_list:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")
  
  def _vertex_degree_matrix(self, index):
    for vertex in self.vertices:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")

  def remove_edge(self, edge):
    if self.is_representation_list:
      self._remove_edge_list(edge)
    else:
      self._remove_edge_matrix(edge)
    
  def _remove_edge_list(self, edge):
    if edge in self.edges:
      self.edges.remove(edge)
      return

    reversed_edge = tuple(reversed(edge))
    if reversed_edge in self.edges:
      self.edges.remove(reversed_edge)
      
  def _remove_edge_matrix(self, vertex1, vertex2):
    if vertex1 in self.vertices and vertex2 in self.vertices:
      if self.has_edge(vertex1, vertex2):
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
    print("Quantidade de vértices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
    print("Arestas:", self.get_edges())
    for vertex in self.adjacency_list:
      print("Grau:", vertex.degree, "|", vertex.data, "->",
            [neighbor.data for neighbor in self.adjacency_list[vertex]])
  
  def print_matrix(self):
    print("Quantidade de vertices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
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

graph = Graph("list")
graph_2 = Graph("list")

vertex_a = Vertex("A", 0)
vertex_b = Vertex("B", 1)
# vertex_c = Vertex("C", 2)
# vertex_d = Vertex("D", 3)
# vertex_e = Vertex("E", 4)

# graph.add_vertex_matrix(vertex_a)
# graph.add_vertex_matrix(vertex_b)

graph_2.add_vertex(vertex_a)
graph_2.add_vertex(vertex_b)
# graph.add_vertex_matrix(vertex_c)
# graph.add_vertex_matrix(vertex_d)
# graph.add_vertex_matrix(vertex_e)

graph_2.add_edge(vertex_a, vertex_b)
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