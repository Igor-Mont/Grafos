from graph import Graph
from graph import Vertex
from graph import Passeio
from graph import passeio_using_dfs, print_passeio, print_reversed_passeio, section_passeio, caminho_using_dfs, dfs_cycle, dfs_cycle_proof, components, does_not_have_circuit, is_connected, extra2
def main():
  
  graph = Graph("list")

  vertexA = Vertex("A", 1)
  vertexB = Vertex("B", 2)
  vertexC = Vertex("C", 3)
  vertexD = Vertex("D", 4)
  vertexE = Vertex("E", 5)
  vertexF = Vertex("F", 6)

  graph.add_vertex(vertexA)
  graph.add_vertex(vertexB)
  graph.add_vertex(vertexC)
  graph.add_vertex(vertexD)
  graph.add_vertex(vertexE)
  graph.add_vertex(vertexF)

  graph.add_edge(vertexA, vertexB)
  graph.add_edge(vertexA, vertexC)

  graph.add_edge(vertexB, vertexD)

  graph.add_edge(vertexC, vertexD)
  graph.add_edge(vertexC, vertexE)

  graph.add_edge(vertexD, vertexE)
  graph.add_edge(vertexD, vertexF)
  
  passeio = Passeio()
  passeio.add_component(vertexA)
  passeio.add_component(vertexB)
  passeio.add_component(vertexD)
  passeio.add_component(vertexA)
  passeio.add_component(vertexB)
  passeio.add_component(vertexD)
  passeio.add_component(vertexB)
  passeio.add_component(vertexD)
  passeio.add_component(vertexC)
  
  print("Funcao 5.2, exemplo de passeio:")
  print_passeio(passeio)
  print()
  print("Funcao 5.3, reverso do passeio:")
  print_reversed_passeio(passeio)
  print()
  print("Funcao 5.4, secao do passeio, com indices 0 e 3:")
  section = section_passeio(passeio, 0, 3)
  print([vertex.data for vertex in section])
  print()
  print("Funcao 5.5, passeio no grafo dado vertex A e vertex D")
  print_passeio(passeio_using_dfs(graph, vertexA, vertexD))
  print()
  print("Funcao 5.6, caminho no grafo dado vertex A e vertex D")
  print(caminho_using_dfs(graph, vertexA, vertexF))
  print()
  print("Funcao 5.7, verificar ciclo no grafo")
  dfs_cycle(graph, vertexA)
  print()
  print("Funcao 5.8, verificar ciclo no grafo a partir da ideia de prova")
  print(dfs_cycle_proof(graph, vertexA, vertexF))
  print()
  print("Funcao 5.10, componentes de um grafo")
  components(graph)
  print()
  print("Funcao 5.11, verificar se não existe circuitos")
  if does_not_have_circuit(graph):
    print("não existem circuitos, ou não respita alguma das condições")
  else:
    print("existem circuitos")
  print()
  print("Funcao 5.12, verificar se é conexo")
  if is_connected(graph, vertexA):
    print("É conexo")
  else:
    print("Não é conexo")
  print()
  print("Extra2:")
  extra2(vertexA, vertexC, passeio)
  
if __name__ == "__main__":
  main()