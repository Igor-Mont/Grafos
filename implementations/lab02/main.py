from graph import Graph
from graph import Vertex
from graph_utils import create_complete_graph_kn
from graph_utils import create_graph_kregular

def exemplo1():
  graph = create_complete_graph_kn(5)

  graph.print_graph()
  
def exemplo2():
  graph = create_graph_kregular(10, 3)

  graph.print_graph()

def exemplo3():
  graph = Graph("list")

  vertex1 = Vertex("A", 1)
  vertex2 = Vertex("B", 2)
  vertex3 = Vertex("C", 3)
  vertex4 = Vertex("D", 4)
  vertex5 = Vertex("E", 5) 
  vertex6 = Vertex("F", 6) 

  graph.add_vertex(vertex1)
  graph.add_vertex(vertex2)
  graph.add_vertex(vertex3)
  
  graph.add_vertex(vertex4)
  graph.add_vertex(vertex5)
  graph.add_vertex(vertex6)

  graph.add_edge(vertex1, vertex4)
  graph.add_edge(vertex1, vertex5)
  graph.add_edge(vertex1, vertex6)
  
  graph.add_edge(vertex2, vertex4)
  graph.add_edge(vertex2, vertex6)
  
  graph.add_edge(vertex3, vertex4)
  
  X = {vertex1, vertex2, vertex3}
  Y = {vertex4, vertex5, vertex6}
  
  graph.print_graph()
  print("O grafo {} bipartido".format("é" if graph.is_bipartite_graph(X, Y) else "não é"))

def exemplo4():
  graph = Graph("list")

  vertex1 = Vertex("A", 1)
  vertex2 = Vertex("B", 2)
  vertex3 = Vertex("C", 3)
  vertex4 = Vertex("D", 4)
  vertex5 = Vertex("E", 5) 
  vertex6 = Vertex("F", 6) 

  graph.add_vertex(vertex1)
  graph.add_vertex(vertex2)
  graph.add_vertex(vertex3)
  
  graph.add_vertex(vertex4)
  graph.add_vertex(vertex5)
  graph.add_vertex(vertex6)

  graph.add_edge(vertex1, vertex4)
  graph.add_edge(vertex1, vertex3)
  graph.add_edge(vertex1, vertex5)
  graph.add_edge(vertex1, vertex6)
  
  graph.add_edge(vertex2, vertex4)
  graph.add_edge(vertex2, vertex6)
  graph.add_edge(vertex2, vertex1)
  
  graph.add_edge(vertex3, vertex4)
  graph.add_edge(vertex5, vertex4)
  
  X = {vertex1, vertex2, vertex3}
  Y = {vertex4, vertex5, vertex6}
  
  graph.print_graph()
  print("O grafo {} bipartido".format("é" if graph.is_bipartite_graph(X, Y) else "não é"))

def exemplo5():
  graph = Graph("list")

  vertex1 = Vertex("A", 1)

  graph.add_vertex(vertex1)
  
  X = {vertex1}
  Y = { }
  
  graph.print_graph()
  print("O grafo {} bipartido".format("é" if graph.is_bipartite_graph(X, Y) else "não é"))
  
def exemplo6():
  graph = Graph("list")
  
  X = { }
  Y = { }
  
  graph.print_graph()
  print("O grafo {} bipartido".format("é" if graph.is_bipartite_graph(X, Y) else "não é"))
 
def exemplo7():
  graph = Graph("list")

  vertex1 = Vertex("A", 1)
  vertex2 = Vertex("B", 2)
  vertex3 = Vertex("C", 3)
  vertex4 = Vertex("D", 4)

  graph.add_vertex(vertex1)
  graph.add_vertex(vertex2)
  
  graph.add_vertex(vertex3)
  graph.add_vertex(vertex4)
  

  graph.add_edge(vertex1, vertex4)
  graph.add_edge(vertex1, vertex3)
  
  graph.add_edge(vertex2, vertex4)  
  graph.add_edge(vertex2, vertex3)  
  
  X = {vertex1, vertex2}
  Y = {vertex4} #vertex3 esta fora
  
  graph.print_graph()
  print("O grafo {} bipartido".format("é" if graph.is_bipartite_graph(X, Y) else "não é"))
  
def main():
  print("EXEMPLO 1:\n")
  exemplo1()
  print("\nEXEMPLO 2:\n")
  exemplo2()
  print("\nEXEMPLO 3:\n")
  exemplo3()
  print("\nEXEMPLO 4:\n")
  exemplo4()
  print("\nEXEMPLO 5:\n")
  exemplo5()
  print("\nEXEMPLO 6:\n")
  exemplo6()
  print("\nEXEMPLO 7:\n")
  exemplo7()

if __name__ == "__main__":
  main()