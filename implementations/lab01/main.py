from graph import Graph
from graph import Vertex

def exemplo1():
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
  graph.add_edge(vertex_b, vertex_e)
  graph.add_edge(vertex_c, vertex_c)
  graph.add_edge(vertex_c, vertex_d)
  graph.add_edge(vertex_d, vertex_e)

  graph.print_graph()

  graph = Graph("matrix") 

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
  graph.add_edge(vertex_b, vertex_e)
  graph.add_edge(vertex_c, vertex_c)
  graph.add_edge(vertex_c, vertex_d)
  graph.add_edge(vertex_d, vertex_e)

  graph.print_graph()
  
def exemplo2():
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
  graph.add_edge(vertex_a, vertex_c)
  graph.add_edge(vertex_a, vertex_d)
  graph.add_edge(vertex_a, vertex_e)
  graph.add_edge(vertex_b, vertex_c)
  graph.add_edge(vertex_b, vertex_d)
  graph.add_edge(vertex_b, vertex_e)
  graph.add_edge(vertex_c, vertex_d)
  graph.add_edge(vertex_c, vertex_e)
  graph.add_edge(vertex_d, vertex_e)

  graph.print_graph()

  graph = Graph("matrix")

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
  graph.add_edge(vertex_a, vertex_c)
  graph.add_edge(vertex_a, vertex_d)
  graph.add_edge(vertex_a, vertex_e)
  graph.add_edge(vertex_b, vertex_c)
  graph.add_edge(vertex_b, vertex_d)
  graph.add_edge(vertex_b, vertex_e)
  graph.add_edge(vertex_c, vertex_d)
  graph.add_edge(vertex_c, vertex_e)
  graph.add_edge(vertex_d, vertex_e)

  graph.print_graph()

def main():
  print("EXEMPLO 1:\n")
  exemplo1()
  print("EXEMPLO 2:\n")
  exemplo2()

if __name__ == "__main__":
  main()