from graph import Graph
from graph import Vertex

def main():
  graph = Graph("list")

  vertexX = Vertex("X", 1)
  vertexW = Vertex("W", 2)
  vertexV = Vertex("V", 3)
  vertexY = Vertex("Y", 4)
  vertexU = Vertex("U", 5)

  graph.add_vertex(vertexX)
  graph.add_vertex(vertexW)
  graph.add_vertex(vertexV)
  graph.add_vertex(vertexY)
  graph.add_vertex(vertexU)
  

  graph.add_edge(vertexX, vertexY)
  graph.add_edge(vertexX, vertexW)
  
  graph.add_edge(vertexW, vertexY)  
  graph.add_edge(vertexW, vertexV)
   
  graph.add_edge(vertexY, vertexV) 
  graph.add_edge(vertexY, vertexV) 
  graph.add_edge(vertexY, vertexU)
   
  graph.add_edge(vertexV, vertexU) 
  # print("\nGrafo Principal\n")

  # graph.print_graph();
  
  # # A)
  # print("\nExemplo A\n")
  
  # Hx = [vertexX, vertexU, vertexY]
  # He = [(vertexX, vertexY), (vertexY, vertexU)]
  
  # subgraphOwn = graph.generate_subgraph(Hx, He)
  # subgraphOwn.print_graph()
    
  # # B)
  # print("\nExemplo B\n")
  
  # x = [vertexX, vertexU, vertexY, vertexV]
  # subgraphInducedX = graph.induced_graph(x)
  # subgraphInducedX.print_graph()
  
  # # C)
  # print("\nExemplo C\n")
  
  # x1 = [vertexY, vertexV, vertexX, vertexU]
  # subgraphInducedX1 = graph.induced_graph(x1)
  # subgraphInducedX1.print_graph()
  
  # # D)
  # print("\nExemplo D\n")
  
  # x2 = [vertexU, vertexW]
  # subgraphInducedX2 = graph.vertex_subtraction(x2)
  # subgraphInducedX2.print_graph()
  
  # # E)
  print("\nExemplo E\n")
  
  E1 = [(vertexV, vertexU), (vertexX, vertexW), (vertexY, vertexU), (vertexY, vertexV), (vertexY, vertexV)]
  subgraphInducedE1 = graph.edge_induced_graph(E1)
  subgraphInducedE1.print_graph();
  
  # # F)
  # print("\nExemplo F\n")
  
  # E2 = [(vertexV, vertexU), (vertexW, vertexV), (vertexY, vertexV)]
  # subgraphInducedE2 = graph.edge_subtraction(E2)
  # subgraphInducedE2.print_graph();
   

if __name__ == "__main__":
  main()