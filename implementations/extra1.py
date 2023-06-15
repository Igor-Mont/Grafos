import math
import tkinter as tk

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
      self._add_edge_matrix(vertex1, vertex2)

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

  def print_graph(self):
    if self.is_representation_list:
      self._print_list()
    else:
      self._print_matrix()

  def _print_list(self):
    print("Quantidade de vértices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
    print("Arestas:", self.get_edges())
    for vertex in self.adjacency_list:
      neighbors_data = [neighbor.data for neighbor in self.adjacency_list[vertex]]
      print("Grau: {} | {} -> {}".format(vertex.degree, vertex.data, neighbors_data))
  
  def _print_matrix(self):
    print("Quantidade de vertices:", len(self.get_vertices()))
    print("Quantidade de arestas:", self.get_edge_count())
    print("Arestas:", self.get_edges())

    print(" "*12, end="")
    for vertex in self.vertices:
      print(vertex.data, end=" ")
    print()

    for i in range(len(self.vertices)):
      vertex = self.vertices[i]
      print("Grau: {} | {}".format(vertex.degree, vertex.data), end=" ")
      for j in range(len(self.vertices)):
        print(self.matrix[i][j], end=" ")
      print()

graph = Graph("list")

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

graph.add_edge(vertex_a, vertex_b)
graph.add_edge(vertex_b, vertex_c)
graph.add_edge(vertex_b, vertex_d)
graph.add_edge(vertex_b, vertex_e)
graph.add_edge(vertex_c, vertex_c)
graph.add_edge(vertex_c, vertex_d)
graph.add_edge(vertex_d, vertex_e)
graph.add_edge(vertex_e, vertex_b)

class GrafoGUI:
    def __init__(self, graph, edges):
        self.graph = graph
        self.edges = edges
        self.positions = list()
        self.actual_count = 0
        self.radius = 20
        self.janela = tk.Tk()
        self.janela.title("Representação Gráfica de Grafo")
        self.canvas = tk.Canvas(self.janela, width=500, height=500)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onclick)
        self.janela.mainloop()

    def onclick(self, event):
        vertex = list(self.graph.keys())[self.actual_count]
        x, y = event.x, event.y
        self.positions.append((x, y))
        self.desenhar_vertice(x, y, vertex.index)
        self.actual_count += 1

        if self.actual_count == len(self.graph.keys()):
          self.desenhar_arestas()
          return
        

    def desenhar_vertice(self, x, y, vertice):
        self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill="lightblue")
        self.canvas.create_text(x, y, text=str(vertice), fill="black")

    def desenhar_arestas(self):
      self.canvas.delete("arestas")

      edge_counts = {}  # Dicionário para rastrear a contagem de ocorrências de cada aresta
      print("EDGES", self.edges, self.edges[0])
      print("EDGES COUNT", edge_counts)
      for edge in self.edges:
        # or tuple(reversed(edge)) in edge_counts
        if tuple(reversed(edge)) in edge_counts:
          edge_counts[tuple(reversed(edge))] += 1
          continue
        if edge in edge_counts:
          print("INN")
          print(edge, tuple(reversed(edge)))
          print(edge_counts[edge])
          edge_counts[edge] += 1
          
        else:
          edge_counts[edge] = 1
      print("EDGES COUNT", edge_counts)

      for edge in edge_counts:
        vertex1_data, vertex2_data = edge
        vertex1 = None
        vertex2 = None

        for vertex in self.graph.keys():
          if vertex.data == vertex1_data:
            vertex1 = vertex
          if vertex.data == vertex2_data:
            vertex2 = vertex

        if vertex1 and vertex2:
          x1, y1 = self.positions[vertex1.index - 1]
          x2, y2 = self.positions[vertex2.index - 1]

          if x1 == x2 and y1 == y2:
            # Desenhar um loop
            loop_radius = self.radius * 1.5
            self.canvas.create_arc(x1 - loop_radius, y1 - loop_radius, x1, y1 + loop_radius, start=0, extent=50000,
                                  style=tk.ARC, outline="red", tags="arestas")
          else:
            edge_count = edge_counts[edge]
            print("COUNT", edge_count)
            if edge_count > 1:
              print("multipla")
              # Desenhar um arco para arestas paralelas

              for i in range(edge_count):
                if i % 2 != 0:
                  self.canvas.create_line(x1, y1, x2, y2, fill="black", tags="arestas")
                  continue
                print((x1, y1), (x2, y2))
                center_x = int((x1 + x2) / 2) + 50
                center_y = int((y1 + y2) / 2) + 50
                self.canvas.create_line(x1, y1, center_x, center_y, x2, y2, smooth=True, splinesteps=20, width=2, fill="red", tags="arestas")
            else:
              self.canvas.create_line(x1, y1, x2, y2, fill="black", tags="arestas")



grafo_gui = GrafoGUI(graph.adjacency_list, graph.get_edges())
