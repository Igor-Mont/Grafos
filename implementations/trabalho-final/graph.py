from linked_list import LinkedList

class Vertex:
  def __init__(self, data, index):
    self.data = data
    self.index = index
    self.degree = 0

class Edge:
  def __init__(self, v1, v2, weight):
    self._v1 = v1
    self._v2 = v2
    self._weight = weight
  
  def get_vertices(self, only_data=False):
    if only_data:
      return self._v1.data, self._v2.data
    return self._v1, self._v2

  def get_weight(self):
    return self._weight
  
  def get_tuple(self, only_data=True):
    if only_data:
      return (self._v1.data, self._v2.data)
    return (self._v1, self._v2)

class Graph:
  def __init__(self):
    self._edge_count = 0
    self.adjacency_list = dict()
    self.edges_list = list()

  def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
      self.adjacency_list[vertex] = LinkedList()
      
  def get_edge_count(self):
    return self._edge_count

  def add_edge(self, edge):
    vertex1, vertex2 = edge.get_vertices()
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      self._update_vertex_degrees(vertex1, vertex2)
      self.adjacency_list[vertex1].append(vertex2)
      self.adjacency_list[vertex2].append(vertex1)
      self.edges_list.append(edge)
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

  def get_vertices(self, only_data=True):
    if only_data:
      return [vertex.data for vertex in self.adjacency_list.keys()]
    return [vertex for vertex in self.adjacency_list.keys()]

  def get_edges(self,  filtered=False, only_data=True):
    filtered_edges = []
    if filtered:
      for edge in self.edges_list:
        edge = edge.get_tuple(only_data)
        sorted_edge = tuple(sorted(edge))
        if sorted_edge not in filtered_edges:
          filtered_edges.append(edge)
      return filtered_edges
    return [edge.get_tuple(only_data) for edge in self.edges_list]
  
  def has_edge(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      return vertex2 in self.adjacency_list[vertex1] and vertex1 in self.adjacency_list[vertex2]
    return False
  
  def neighboring_vertices(self, index_v1, index_v2):
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

  def vertex_degree(self, index):
    for vertex in self.adjacency_list:
      if vertex.index == index:
        return vertex.degree
    raise IndexError("list index out of range")
  
  def get_vertex_by_data(self, data):
    for vertex in self.adjacency_list:
      if vertex.data == data:
        return vertex
    return None
  
  def remove_edge(self, edge):
    vertex1, vertex2 = edge.get_vertices()
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
      if self.has_edge(vertex1, vertex2):
        self._update_vertex_degrees(vertex1, vertex2, increment=False)
        if edge in self.edges_list:
          self.edges_list.remove(edge)
          self.adjacency_list[vertex1].remove(vertex2)
          self.adjacency_list[vertex2].remove(vertex1)
          self._edge_count -= 1
      else:
        raise ValueError("Edge does not exist in the graph.")
    else:
      raise ValueError("One or both vertices do not exist in the graph.")
      
  def print_graph(self):
    print("Estrutura de adjacência")
    print("Quantidade de vértices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
    print("Arestas:", self.get_edges())
    for vertex in self.adjacency_list:
      neighbors_data = [neighbor.data for neighbor in self.adjacency_list[vertex]]
      print("Grau: {} | {} -> {}".format(vertex.degree, vertex.data, neighbors_data))

graph = Graph() 

vertex_a = Vertex("A", 1)
vertex_b = Vertex("B", 2)
vertex_c = Vertex("C", 3)
vertex_d = Vertex("D", 4)
vertex_e = Vertex("E", 5) 

graph.add_vertex(vertex_a)
graph.add_vertex(vertex_b)
graph.add_vertex(vertex_c)
graph.add_vertex(vertex_d)
graph.add_vertex(vertex_e)

edge_a = Edge(vertex_a, vertex_b, 1)
edge_b = Edge(vertex_b, vertex_c, 2)
edge_c = Edge(vertex_b, vertex_d, 3)
edge_d = Edge(vertex_b, vertex_e, 4)
edge_e = Edge(vertex_b, vertex_e, 5)
edge_f = Edge(vertex_c, vertex_c, 6)
edge_g = Edge(vertex_c, vertex_d, 7)
edge_h = Edge(vertex_d, vertex_e, 8)

graph.add_edge(edge_a)
graph.add_edge(edge_b)
graph.add_edge(edge_c)
graph.add_edge(edge_d)
graph.add_edge(edge_e)
graph.add_edge(edge_f)
graph.add_edge(edge_g)
graph.add_edge(edge_h)

graph.print_graph()

graph.remove_edge(edge_a)
graph.remove_edge(edge_b)
graph.remove_edge(edge_c)
graph.remove_edge(edge_d)
graph.remove_edge(edge_e)
graph.remove_edge(edge_f)
graph.remove_edge(edge_g)
graph.remove_edge(edge_h)

graph.print_graph()
