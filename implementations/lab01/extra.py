from graph import Graph
from graph import Vertex
import math
import tkinter as tk

class GrafoGUI:
  def __init__(self, graph):
    self.graph = graph
    self.strucuture = graph.adjacency_list if graph.is_representation_list else graph.matrix
    self.edges = graph.get_edges()
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
    if self.graph.is_representation_list:
      vertex = list(self.strucuture.keys())[self.actual_count]
    else: 
      vertex = list(self.graph.vertices_matrix)[self.actual_count]
    x, y = event.x, event.y
    self.positions.append((x, y))
    self.desenhar_vertice(x, y, vertex.data)
    self.actual_count += 1

    if self.actual_count == len(self.strucuture):
      self.desenhar_arestas()
      return
        
  def desenhar_vertice(self, x, y, vertice):
      self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill="lightblue")
      self.canvas.create_text(x, y, text=str(vertice), fill="black")

  def contar_arestas(self):
    edge_counts = {}
    for edge in self.edges:
        if tuple(reversed(edge)) in edge_counts:
            edge_counts[tuple(reversed(edge))] += 1
            continue
        if edge in edge_counts:
            edge_counts[edge] += 1
        else:
            edge_counts[edge] = 1
    return edge_counts
  
  def desenhar_lacos(self, x, y, edge_count):
    if edge_count > 1:
      self.canvas.create_text(x, y - 50, text=str(edge_count) + " laços", fill="black")
    self.canvas.create_arc(x - 15, y - 38, x + 15, y - 10, start=330, extent=250,
                           style=tk.ARC, outline="red", tags="arestas")

  def desenhar_arestas_paralelas(self, x1, y1, x2, y2, edge_count):
     for i in range(edge_count):
        if i == 0:
          self.canvas.create_line(x1, y1, x2, y2, fill="black", tags="arestas")
          continue
        if i % 2 != 0:
          center_x = int((x1 + x2) / 2) + 30
          center_y = int((y1 + y2) / 2) + 30
          self.canvas.create_line(x1, y1, center_x + (i * 10) , center_y + (i * 10), x2, y2, smooth=True, splinesteps=20, fill="red", tags="arestas")
          continue
        center_x = int((x1 + x2) / 2) - 30
        center_y = int((y1 + y2) / 2) - 30
        self.canvas.create_line(x1, y1, center_x - (i * 10) , center_y - (i * 10), x2, y2, smooth=True, splinesteps=20, fill="red", tags="arestas")

  def desenhar_arestas(self):
    self.canvas.delete("arestas")
    edge_counts = self.contar_arestas()

    for edge in edge_counts:
      vertex1_data, vertex2_data = edge
      vertex1 = self.graph.get_vertex_by_data(vertex1_data)
      vertex2 = self.graph.get_vertex_by_data(vertex2_data)

      if vertex1 and vertex2:
        x1, y1 = self.positions[vertex1.index - 1]
        x2, y2 = self.positions[vertex2.index - 1]

        edge_count = edge_counts[edge]
        if edge_count > 1:
          if x1 == x2 and y1 == y2:
            self.desenhar_lacos(x1, y1, edge_count)
          else:
            self.desenhar_arestas_paralelas(x1, y1, x2, y2, edge_count)
        else:
          if x1 == x2 and y1 == y2:
            self.desenhar_lacos(x1, y1, edge_count)
          else:
            self.canvas.create_line(x1, y1, x2, y2, fill="black", tags="arestas")

graph = Graph("list")

vertexA = Vertex("A", 1)
vertexB = Vertex("B", 2)
vertexC = Vertex("C", 3)
vertexE = Vertex("E", 4)

graph.add_vertex(vertexA)
graph.add_vertex(vertexB)
graph.add_vertex(vertexC)
graph.add_vertex(vertexE)

graph.add_edge(vertexA, vertexB)
graph.add_edge(vertexB, vertexC)
graph.add_edge(vertexC, vertexE) 

grafo_gui = GrafoGUI(graph) 
