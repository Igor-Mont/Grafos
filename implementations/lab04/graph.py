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
      self.vertices_matrix = list()
      return
    elif self.is_representation_list:
      self.adjacency_list = dict()
      self.edges_list = list()
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
    if vertex not in self.vertices_matrix:
      self.vertices_matrix.append(vertex)
      self.matrix.append([0] * len(self.vertices_matrix))
      for row in self.matrix[:-1]:
        row.append(0)

  def get_edge_count(self):
    return self._edge_count

  def add_edge(self, vertex1, vertex2):
    if self.is_representation_list:
      self._add_edge_list(vertex1, vertex2)
    else:
      self._add_edge_matrix(vertex1, vertex2)

  def _add_edge_list(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      self._update_vertex_degrees(vertex1, vertex2)
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)
      edge = (vertex1.data, vertex2.data)
      self.edges_list.append(edge)
      self._edge_count += 1
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")
    
  def _add_edge_matrix(self, vertex1, vertex2):
    if vertex1 in self.vertices_matrix and vertex2 in self.vertices_matrix:
      index1, index2 = self._get_vertices_matrix_index(vertex1, vertex2)
      self._update_vertex_degrees(vertex1, vertex2)
      self._update_matrix_entries(index1, index2)
      edge = (vertex1.data, vertex2.data)
      self.edges_matrix.append(edge)
      self._edge_count += 1
    else:
      raise ValueError("One or both vertexes do not exist in the graph.")
  
  def _update_vertex_degrees(self, vertex1, vertex2, increment=True):
    if increment:
      vertex1.degree += 1
      vertex2.degree += 1
    else:
      vertex1.degree -= 1
      vertex2.degree -= 1

  def _update_matrix_entries(self, index1, index2, increment=True):
    if increment:
      self.matrix[index1][index2] += 1
      self.matrix[index2][index1] += 1
    else:
      self.matrix[index1][index2] -= 1
      self.matrix[index2][index1] -= 1
      
  def _get_vertices_matrix_index(self, vertex1, vertex2):
    index1 = self.vertices_matrix.index(vertex1)
    index2 = self.vertices_matrix.index(vertex2)
    return index1, index2

  def _get_vertices_matrix_index(self, vertex1, vertex2):
    index1 = self.vertices_matrix.index(vertex1)
    index2 = self.vertices_matrix.index(vertex2)
    return index1, index2

  def get_vertices(self, only_data=True):
    if self.is_representation_list:
      return self._get_vertices_list(only_data)
    else:
      return self._get_vertices_matrix(only_data)
  
  def _get_vertices_list(self, only_data):
    if only_data:
      return [vertex.data for vertex in self.adjacency_list.keys()]
    return [vertex for vertex in self.adjacency_list.keys()]

  def _get_vertices_matrix(self, only_data):
    if only_data:
      return [vertex.data for vertex in self.vertices_matrix]
    return [vertex for vertex in self.vertices_matrix]

  def get_edges(self, filtered=False):
    if self.is_representation_list:
      return self._get_edges_list(filtered)
    else:
      return self._get_edges_matrix(filtered)
    
  def _get_edges_list(self,  filtered=False):
    filtered_edges = []
    if filtered:
      for edge in self.edges_list:
        sorted_edge = tuple(sorted(edge))
        if sorted_edge not in filtered_edges:
          filtered_edges.append(edge)
      return filtered_edges
    return self.edges_list
  
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
    if(self.vertices_matrix[0].index == 0):
      return self.matrix[vertex1.index][vertex2.index] >= 1
      
    return self.matrix[vertex1.index-1][vertex2.index-1] >= 1

  def neighboring_vertices(self, index_v1, index_v2):
    if self.is_representation_list:
      return self._neighboring_vertices_list(index_v1, index_v2)
    else:
      return self._neighboring_vertices_matrix(index_v1, index_v2)
  
  def _neighboring_vertices_list(self, index_v1, index_v2):
    vertex1 = None
    vertex2 = None
    for vertex in self.adjacency_list:
      if vertex.index == index_v1:
        vertex1 = vertex
      if vertex.index == index_v2:
        vertex2 = vertex

    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      return vertex2 in self.adjacency_list[vertex1] and vertex1 in self.adjacency_list[vertex2]
    return False

  def _neighboring_vertices_matrix(self, index_v1, index_v2):
    if(self.vertices_matrix[0].index == 0):
      return self.matrix[index_v1][index_v2] >= 1
      
    return self.matrix[index_v1-1][index_v2-1] >= 1
  
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
  
  def get_vertex_by_data(self, data):
    if self.is_representation_list:
      return self._get_vertex_by_data_list(data)
    else:
      return self._get_vertex_by_data_matrix(data)
    
  def _get_vertex_by_data_list(self, data):
    for vertex in self.adjacency_list:
      if vertex.data == data:
        return vertex
    return None
  
  def _get_vertex_by_data_matrix(self, data):
    for vertex in self.vertices_matrix:
      if vertex.data == data:
        return vertex
    return None

  def get_vertex_by_data(self, data):
    if self.is_representation_list:
      return self._get_vertex_by_data_list(data)
    else:
      return self._get_vertex_by_data_matrix(data)
  
  def _vertex_degree_matrix(self, index):
    for vertex in self.vertices_matrix:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")

  def remove_edge(self, vertex1, vertex2):
    if self.is_representation_list:
      self._remove_edge_list(vertex1, vertex2)
    else:
      self._remove_edge_matrix(vertex1, vertex2)
    
  def _remove_edge_list(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      if self.has_edge(vertex1, vertex2):
        self._update_vertex_degrees(vertex1, vertex2, increment=False)
        edge = (vertex1.data, vertex2.data)
        if edge in self.edges_list:
          self.edges_list.remove(edge)
          self.adjacency_list[vertex1].remove(vertex2)
          self.adjacency_list[vertex2].remove(vertex1)
          self._edge_count -= 1
      else:
        raise ValueError("Edge does not exist in the graph.")
    else:
      raise ValueError("One or both vertices do not exist in the graph.")
      
  def _remove_edge_matrix(self, vertex1, vertex2):
    if vertex1 in self.vertices_matrix and vertex2 in self.vertices_matrix:
      if self.has_edge(vertex1, vertex2):
        index1, index2 = self._get_vertices_matrix_index(vertex1, vertex2)
        self._update_vertex_degrees(vertex1, vertex2, increment=False)
        self._update_matrix_entries(index1, index2, increment=False)
        edge = (vertex1.data, vertex2.data)
        if edge in self.edges_matrix:
          self.edges_matrix.remove(edge)
          self._edge_count -= 1
      else:
        raise ValueError("Edge does not exist in the graph.")
    else:
      raise ValueError("One or both vertices do not exist in the graph.")
  
  def generate_subgraph(self, vertices, edges):
    subgraph = Graph("list")
    new_vertices = [Vertex(vertex.data, vertex.index) for vertex in vertices]

    for vertex in new_vertices:
      subgraph.add_vertex(vertex)
    
    new_edges = [(subgraph.get_vertex_by_data(vertex1.data), subgraph.get_vertex_by_data(vertex2.data)) for vertex1, vertex2 in edges]
    for vertex1, vertex2 in new_edges:
      v1 = self.get_vertex_by_data(vertex1.data)
      v2 = self.get_vertex_by_data(vertex2.data)
      if(self.has_edge(v1, v2)):
        subgraph.add_edge(vertex1, vertex2)
    
    return subgraph

  def induced_graph(self, vertices):
    subgraph = Graph("list")
    new_vertices = [Vertex(vertex.data, vertex.index) for vertex in vertices]

    for vertex in new_vertices:
      subgraph.add_vertex(vertex)
    
    for vertex_data_1, vertex_data_2 in self.get_edges():
      v1 = self.get_vertex_by_data(vertex_data_1)
      v2 = self.get_vertex_by_data(vertex_data_2)
      vertices_subgraph = subgraph.get_vertices(only_data=False)
      vertex1 = subgraph.get_vertex_by_data(v1.data)
      vertex2 = subgraph.get_vertex_by_data(v2.data)
      if vertex1 in vertices_subgraph and vertex2 in vertices_subgraph:
          if self.has_edge(v1, v2):
            subgraph.add_edge(vertex1, vertex2)
    
    return subgraph

  def edge_induced_graph(self, edges):
    subgraph = Graph("list")
    current_edges = [(vertex1.data, vertex2.data) for vertex1, vertex2 in edges]
    for edge in self.get_edges():
        if edge in current_edges:
          data1, data2 = edge
          vertex1 = self.get_vertex_by_data(data1)
          vertex2 = self.get_vertex_by_data(data2)
          v1 = subgraph.get_vertex_by_data(vertex1.data)
          if not vertex1.data in subgraph.get_vertices():
            v1 = Vertex(vertex1.data, vertex1.index)
          v2 = subgraph.get_vertex_by_data(vertex2.data)
          if not vertex2.data in subgraph.get_vertices():
            v2 = Vertex(vertex2.data, vertex2.index)
          subgraph.add_vertex(v1)
          subgraph.add_vertex(v2)
          subgraph.add_edge(v1, v2)

    return subgraph

  def edge_subtraction(self, edges):
    subgraph = Graph("list")
    current_edges = [(vertex1.data, vertex2.data) for vertex1, vertex2 in edges]
    
    for edge in self.get_edges():
      if not edge in current_edges:
        vertex1_data, vertex2_data = edge
        v1 = self.get_vertex_by_data(vertex1_data)
        v2 = self.get_vertex_by_data(vertex2_data)
        if not vertex1_data in subgraph.get_vertices():
          new_vertex1 = Vertex(v1.data, v1.index)
          subgraph.add_vertex(new_vertex1)
        if not vertex2_data in subgraph.get_vertices():
          new_vertex2 = Vertex(v2.data, v2.index)
          subgraph.add_vertex(new_vertex2)

    for vertex_data_1, vertex_data_2 in self.get_edges():
      v1 = self.get_vertex_by_data(vertex_data_1)
      v2 = self.get_vertex_by_data(vertex_data_2)
      vertices_subgraph = subgraph.get_vertices(only_data=False)
      vertex1 = subgraph.get_vertex_by_data(v1.data)
      vertex2 = subgraph.get_vertex_by_data(v2.data)
      if vertex1 in vertices_subgraph and vertex2 in vertices_subgraph:
        subgraph.add_edge(vertex1, vertex2)

    return subgraph

  def vertex_subtraction(self, vertices):
    subgraph = Graph("list")
    vertices_data = [vertex.data for vertex in vertices]
    for vertex in self.get_vertices(only_data=False):
      if not vertex.data in vertices_data:
        new_vertex = Vertex(vertex.data, vertex.index)
        subgraph.add_vertex(new_vertex)

    for vertex_data_1, vertex_data_2 in self.get_edges():
      v1 = self.get_vertex_by_data(vertex_data_1)
      v2 = self.get_vertex_by_data(vertex_data_2)
      vertices_subgraph = subgraph.get_vertices(only_data=False)
      vertex1 = subgraph.get_vertex_by_data(v1.data)
      vertex2 = subgraph.get_vertex_by_data(v2.data)
      if vertex1 in vertices_subgraph and vertex2 in vertices_subgraph:
          if self.has_edge(v1, v2):
            subgraph.add_edge(vertex1, vertex2)

    return subgraph

  def print_graph(self):
    if self.is_representation_list:
      self._print_list()
    else:
      self._print_matrix()

  def _print_list(self):
    print("Estrutura de adjacência")
    print("Quantidade de vértices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
    print("Arestas:", self.get_edges())
    for vertex in self.adjacency_list:
      neighbors_data = [neighbor.data for neighbor in self.adjacency_list[vertex]]
      print("Grau: {} | {} -> {}".format(vertex.degree, vertex.data, neighbors_data))
  
  def _print_matrix(self):
    print("Matriz de adjacência")
    print("Quantidade de vertices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
    print("Arestas:", self.get_edges())

    print(" "*12, end="")
    for vertex in self.vertices_matrix:
      print(vertex.data, end=" ")
    print()

    for i in range(len(self.vertices_matrix)):
      vertex = self.vertices_matrix[i]
      print("Grau: {} | {}".format(vertex.degree, vertex.data), end=" ")
      for j in range(len(self.vertices_matrix)):
        print(self.matrix[i][j], end=" ")
      print()
    print()