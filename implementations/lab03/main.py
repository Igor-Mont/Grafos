from graph import Graph
from graph import Vertex
from dfs import depth_first_search

def exemplo():
  graph = Graph("list")

  vertex_a = Vertex("A", 1)
  vertex_b = Vertex("B", 2)
  vertex_c = Vertex("C", 3)
  vertex_d = Vertex("D", 4)
  vertex_e = Vertex("E", 5)
  vertex_f = Vertex("F", 6)
  vertex_g = Vertex("G", 7)
  vertex_h = Vertex("H", 8)

  graph.add_vertex(vertex_a)
  graph.add_vertex(vertex_b)
  graph.add_vertex(vertex_c)
  graph.add_vertex(vertex_d)
  graph.add_vertex(vertex_e)
  graph.add_vertex(vertex_f)
  graph.add_vertex(vertex_g)
  graph.add_vertex(vertex_h)

  graph.add_edge(vertex_a, vertex_b)
  graph.add_edge(vertex_a, vertex_c)
  graph.add_edge(vertex_a, vertex_e)
  graph.add_edge(vertex_a, vertex_f)

  graph.add_edge(vertex_b, vertex_d)
  graph.add_edge(vertex_b, vertex_e)

  graph.add_edge(vertex_c, vertex_f)
  graph.add_edge(vertex_c, vertex_g)
  graph.add_edge(vertex_c, vertex_h)

  graph.add_edge(vertex_g, vertex_f)
  graph.add_edge(vertex_f, vertex_h)

  graph.add_edge(vertex_g, vertex_h)

  depth_first_search(graph, vertex_a)
  # graph.print_graph()

def main():
  exemplo()

if __name__ == "__main__":
  main()