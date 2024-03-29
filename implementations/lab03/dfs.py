def check_edge_in_list(edge, list_edges):
  reversed_edge = tuple(reversed(edge))
  return edge in list_edges or reversed_edge in list_edges

def dfs(graph, start_vertex, tree_edges, return_edges):
  start_vertex.set_marked()

  graph.increment_entry_depth()
  start_vertex.set_entry_depth(graph.get_entry_depth())

  for next_vertex in graph.adjacency_list[start_vertex]:
    edge = (start_vertex.data, next_vertex.data)
    is_returned_edge = check_edge_in_list(edge, return_edges)

    if not next_vertex.is_marked():
      tree_edges.append(edge)
      dfs(graph, next_vertex, tree_edges, return_edges)
    elif not check_edge_in_list(edge, tree_edges) and not is_returned_edge:
      return_edges.append(edge)

  graph.increment_exit_depth()        
  start_vertex.set_exit_depth(graph.get_exit_depth())

def depth_first_search(graph, start_vertex):
  tree_edges = list()
  return_edges = list()
  dfs(graph, start_vertex, tree_edges, return_edges)

  graph.reset_marked_vertices()
  graph.reset_depths()

  print("Arestas da Árvore:", tree_edges)
  print("Arestas de Retorno:", return_edges)

  print(" " * 8, end="")
  for vertex in graph.adjacency_list:
    print("{} | ".format(vertex.data), end="")
  print()
  print("PE(v) |", end=" ")
  for vertex in graph.adjacency_list:
    print("{} | ".format(vertex.get_entry_depth()), end="")
  print()
  print("PS(v) |", end=" ")
  for vertex in graph.adjacency_list:
    print("{} | ".format(vertex.get_exit_depth()), end="")
  print()