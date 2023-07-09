from graph import Graph
from graph import Vertex

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