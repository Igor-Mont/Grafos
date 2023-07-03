import random

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0

  def append(self, elem):
    if self.head:
      pointer = self.head

      while (pointer.next):
        pointer = pointer.next

      pointer.next = Node(elem)
    else:
      self.head = Node(elem)
    self._size += 1
  
  def __len__(self):
    return self._size
  
  def _getnode(self, index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else:
        raise IndexError("list index out of range")
      
    return pointer
      
  def __getitem__(self, index):
    pointer = self._getnode(index)
      
    if pointer:
      return pointer.data
    raise IndexError("list index out of range")

  def __setitem__(self, index, elem):
    pointer = self._getnode(index)
      
    if pointer:
      pointer.data = elem
    else:
      raise IndexError("list index out of range")
    
  def index(self, elem):
    pointer = self.head
    i = 0
    while (pointer):
      if pointer.data == elem:
        return i
      pointer = pointer.next
      i += 1
    
    raise ValueError("{} is not in list".format(elem))
  
  def insert(self, index, elem):
    node = Node(elem)
    if index == 0:
      node.next = self.head
      self.head = node
    else:
      pointer = self._getnode(index - 1)
      node.next = pointer.next
      pointer.next = node
    self._size += 1

  def remove(self, elem):
    if self.head == None:
      raise ValueError("{} is not in list".format(elem))
    elif self.head.data == elem:
      self.head = self.head.next
      self._size -= 1
      return True
    else:
      ancestor = self.head
      pointer = self.head.next
      while (pointer):
        if pointer.data == elem:
          ancestor.next = pointer.next
          pointer.next = None
          return True
        ancestor = pointer
        pointer = pointer.next
      self._size -= 1
    raise ValueError("{} is not in list".format(elem))

  def __contains__(self, item):
    current = self.head
    while current:
      if current.data == item:
        return True
      current = current.next
    return False
  
  def __repr__(self):
    r = ""
    pointer = self.head
    while (pointer):
      r += str(pointer.data) + "->"
      pointer = pointer.next
    return r
  
  def __str__(self):
    return self.__repr__()

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
    
  def _vertex_degree_list(self, index):
    for vertex in self.adjacency_list:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")
  
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

  def is_set_disconnected(self, vertices_set):
    for vertex1 in vertices_set:
      for vertex2 in vertices_set:
        if self.has_edge(vertex1, vertex2):
          return False
    return True

  def is_bipartite_graph(self, set_1, set_2):
    intersection_empty = len(list(set(set_1).intersection(set_2))) == 0
    if not intersection_empty:
      return False

    if not self.is_set_disconnected(set_1) or not self.is_set_disconnected(set_2):
      return False
    
    return True
    
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
    print("Somatório do grau dos vértices:", sum([vertex.degree for vertex in self.get_vertices(False)]))
    print("Nº de vértices de grau par:", sum([1 if vertex.degree % 2 == 0 else 0 for vertex in self.get_vertices(False)]))
    print("Nº de vértices de grau ímpar:", sum([1 if vertex.degree % 2 != 0 else 0 for vertex in self.get_vertices(False)]))
    
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
    print("Somatório do grau dos vértices:", sum([vertex.degree for vertex in self.get_vertices(False)]))
    print("Nº de vértices de grau par:", sum([1 if vertex.degree % 2 == 0 else 0 for vertex in self.get_vertices(False)]))
    print("Nº de vértices de grau ímpar:", sum([1 if vertex.degree % 2 != 0 else 0 for vertex in self.get_vertices(False)]))

def create_graph_kn(n_vertices):
  graph = Graph("list")
  for i in range(1, n_vertices+1):
    vertex = Vertex(i, i)
    graph.add_vertex(vertex)

  vertices = graph.get_vertices(False)
  for vertex1 in vertices:
    for vertex2 in vertices:
      if not vertex1.index == vertex2.index and not graph.has_edge(vertex1, vertex2):
        graph.add_edge(vertex1, vertex2)
  
  return graph

def is_odd(n):
  return n % 2 != 0

def create_graph_kregular(n_vertices, k):
  if is_odd(n_vertices) and is_odd(k):
    raise ValueError("By the corollary: In a graph, the number of vertices of degree odd is always even.")

  graph = Graph("list")
  for i in range(1, n_vertices+1):
    vertex = Vertex(i, i)
    graph.add_vertex(vertex)
    
  vertices = graph.get_vertices(only_data=False)
  length = len(vertices)
  
  for i, vertex in enumerate(vertices):
    index = (i + 1) % length
    while not vertex.degree == k:
      next_vertex = vertices[index]
      if vertex.index == next_vertex.index:
        if (vertex.degree + 2 > k):
          index = (index + 1) % length
          continue
      if(vertex.degree < k and next_vertex.degree < k):
        graph.add_edge(vertex, next_vertex)
      index = (index + 1) % length

  return graph

def exemplo1():
  graph = create_graph_kn(5)

  # graph.print_graph()
  
def exemplo2():
  graph = create_graph_kregular(4, 4)

  graph.print_graph()

def exemplo3():
  graph2 = Graph("list")

  vertex1 = Vertex("A", 1)
  vertex2 = Vertex("B", 2)
  vertex3 = Vertex("C", 3)
  vertex4 = Vertex("D", 4)
  vertex5 = Vertex("E", 5) 
  vertex6 = Vertex("F", 6) 

  graph2.add_vertex(vertex1)
  graph2.add_vertex(vertex2)
  graph2.add_vertex(vertex3)
  
  graph2.add_vertex(vertex4)
  graph2.add_vertex(vertex5)
  graph2.add_vertex(vertex6)

  graph2.add_edge(vertex1, vertex4)
  graph2.add_edge(vertex1, vertex5)
  graph2.add_edge(vertex1, vertex6)
  
  graph2.add_edge(vertex2, vertex4)
  graph2.add_edge(vertex2, vertex6)
  
  graph2.add_edge(vertex3, vertex4)
  
  X = {vertex1, vertex2, vertex3}
  Y = {vertex4, vertex5, vertex6}
  
  # graph2.print_graph()
  # print("O grafo {} bipartido".format("é" if graph2.is_bipartite_graph(X, Y) else "não é"))
  
def main():
  print("EXEMPLO 1:\n")
  exemplo1()
  print("\nEXEMPLO 2:\n")
  exemplo2()
  print("\nEXEMPLO 3:\n")
  exemplo3()

if __name__ == "__main__":
  main()