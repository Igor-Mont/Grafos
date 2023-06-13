import tkinter as tk

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
    self.edges = list()

  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = LinkedList()

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


graph = Graph("")

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
        raio = 20
        self.canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill="lightblue")
        self.canvas.create_text(x, y, text=str(vertice), fill="black")

    def desenhar_arestas(self):
      self.canvas.delete("arestas")

      edge_counts = {}  # Dicionário para rastrear a contagem de ocorrências de cada aresta

      for edge in self.edges:
        print(edge in edge_counts, tuple(reversed(edge)) in edge_counts, edge)
        if edge in edge_counts or tuple(reversed(edge)) in edge_counts:
          edge_counts[edge] += 1
        else:
          edge_counts[edge] = 1

      for edge in self.edges:
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
                  loop_radius = 20 * 1.5
                  self.canvas.create_arc(x1 - loop_radius, y1 - loop_radius, x1, y1 + loop_radius, start=0, extent=50000,
                                        style=tk.ARC, outline="red", tags="arestas")
              else:
                  edge_count = edge_counts[edge]
                  if edge_count > 1:
                    print("multipla")
                    # Desenhar um arco para arestas paralelas
                    center_x = (x1 + x2) / 2
                    center_y = (y1 + y2) / 2
                    radius = abs(x2 - x1) / 2

                    if y2 < y1:
                        start_angle = 0
                        extent_angle = -180
                    else:
                        start_angle = 180
                        extent_angle = 180

                    self.canvas.create_arc(
                        center_x - radius,
                        center_y - radius,
                        center_x + radius,
                        center_y + radius,
                        start=start_angle,
                        extent=extent_angle,
                        style=tk.ARC,
                        outline="black",
                        tags="arestas"
                    )
                  else:
                    self.canvas.create_line(x1, y1, x2, y2, fill="black", tags="arestas")



grafo_gui = GrafoGUI(graph.graph, graph.get_edges())
