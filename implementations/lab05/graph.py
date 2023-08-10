from linked_list import LinkedList

class Vertex:
  def __init__(self, data, index):
    self.data = data
    self.index = index
    self.degree = 0
    self._marked = False
    self._entry_depth = 0
    self._exit_depth = 0

  def is_marked(self):
    return self._marked

  def set_marked(self, marked=True):
    self._marked = marked
  
  def set_entry_depth(self, depth):
    self._entry_depth = depth
  
  def set_exit_depth(self, depth):
    self._exit_depth = depth

  def get_entry_depth(self):
    return self._entry_depth

  def get_exit_depth(self):
    return self._exit_depth

class Graph:
  def __init__(self, representation_type):
    self.representation_type = representation_type
    self._edge_count = 0
    self._dfs_entry_depth = 0
    self._dfs_exit_depth = 0
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
  
  def get_entry_depth(self):
    return self._dfs_entry_depth

  def get_exit_depth(self):
    return self._dfs_exit_depth
  
  def increment_entry_depth(self):
    self._dfs_entry_depth += 1
  
  def increment_exit_depth(self):
    self._dfs_exit_depth += 1
  
  def reset_marked_vertices(self):
    for vertex in self.adjacency_list:
      vertex.set_marked(False)
  
  def reset_depths(self):
    self._entry_depth = 0
    self._exit_depth = 0
    
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


class Passeio:
  def __init__(self):
    self.k = 0
    self._sequence = list()
  
  def get_sequence(self):
    return self._sequence
  
  def add_component(self, component):
    if isinstance(component, Vertex):
      self._sequence.append(component)
      self.k += 1
    else:      
      raise Exception("This component is not a vertex.")
  
def print_passeio(passeio):
  first = True
  for component in passeio.get_sequence():
    if first:
      print("{}".format(component.data), end="")
      first = False
    else:
      print(", {}".format(component.data), end="")
  print()

def print_reversed_passeio(passeio):
  components_data = [str(component.data) for component in passeio.get_sequence()]
  reversed_data = reversed(components_data)
  print(", ".join(reversed_data))

def section_passeio(passeio, i, j):
  sequence = passeio.get_sequence()
  section = sequence[i:j+1]
  if j + 1 > len(sequence):
    raise IndexError("List index out of range")
  return section

def check_edge_in_list(edge, list_edges):
  reversed_edge = tuple(reversed(edge))
  return edge in list_edges or reversed_edge in list_edges

find = False
def dfs(graph, start_vertex, end_vertex, passeio):
  start_vertex.set_marked()
  global find

  for next_vertex in graph.adjacency_list[start_vertex]:
    edge = (start_vertex.data, next_vertex.data)
    if find:
      return 

    if not next_vertex.is_marked():
      in_sequence_passeio = end_vertex.data in [vertex.data for vertex in passeio.get_sequence()]
      print(end_vertex.data, end_vertex.data in edge, not in_sequence_passeio, [vertex.data for vertex in passeio.get_sequence()])
      if end_vertex.data in edge and not in_sequence_passeio:
        passeio.add_component(graph.get_vertex_by_data(edge[0]))
        passeio.add_component(graph.get_vertex_by_data(edge[1]))
        print(end_vertex.data, "in", edge)
        find = True
        return

      print("Adicionando: ", edge, end_vertex.data in edge, not in_sequence_passeio)
      passeio.add_component(graph.get_vertex_by_data(edge[0]))
      passeio.add_component(graph.get_vertex_by_data(edge[1]))
      dfs(graph, next_vertex, end_vertex, passeio)

def depth_first_search(graph, start_vertex, end_vertex):
  passeio = Passeio()
  
  dfs(graph, start_vertex, end_vertex, passeio)

  graph.reset_marked_vertices()
  print_passeio(passeio)

def passeio_using_dfs(graph, v, x):
  depth_first_search(graph, v, x)

# passeio 
graph = Graph("list")

vertexA = Vertex("A", 1)
vertexB = Vertex("B", 2)
vertexC = Vertex("C", 3)
vertexD = Vertex("D", 4)
vertexE = Vertex("E", 5)

graph.add_vertex(vertexA)
graph.add_vertex(vertexB)
graph.add_vertex(vertexC)
graph.add_vertex(vertexD)
graph.add_vertex(vertexE)

graph.add_edge(vertexA, vertexB)
graph.add_edge(vertexA, vertexD)

graph.add_edge(vertexB, vertexC)
graph.add_edge(vertexB, vertexD)  
  
graph.add_edge(vertexD, vertexC) 
graph.add_edge(vertexD, vertexC) 
graph.add_edge(vertexD, vertexE)
  
graph.add_edge(vertexC, vertexE) 

passeio = Passeio()
passeio.add_component(vertexA)
passeio.add_component(vertexD)
passeio.add_component(vertexB)
passeio.add_component(vertexC)
print_passeio(passeio)
print_reversed_passeio(passeio)
section = section_passeio(passeio, 0, 3)
print([vertex.data for vertex in section])

passeio_using_dfs(graph, vertexA, vertexE)



