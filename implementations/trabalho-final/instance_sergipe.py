from graph import Graph
from graph import Vertex
from graph import Edge

# Link para ver os vizinhos
# https://www.cidade-brasil.com.br/estado-sergipe.html?c=nom

def instance():
  graph_citys_sergipe = Graph()

  vertex_amparo_de_sao_francisco = Vertex("Amparo de São Francisco", 1)
  vertex_aquidaba = Vertex("Aquidabã", 2)
  vertex_aracaju = Vertex("Aracaju", 3)
  vertex_araua = Vertex("Arauá", 4)
  vertex_areia_branca = Vertex("Areia Branca", 5)
  vertex_barra_dos_coqueiros = Vertex("Barra dos Coqueiros", 6)
  vertex_boquim = Vertex("Boquim", 7)
  vertex_brejo_grande = Vertex("Brejo Grande", 8)
  vertex_campo_do_brito = Vertex("Campo do Brito", 9)
  vertex_canhoba = Vertex("Canhoba", 10)
  vertex_caninde_de_sao_francisco = Vertex("Canindé de São Francisco", 11)
  vertex_capela = Vertex("Capela", 12)
  vertex_carira = Vertex("Carira", 13)
  vertex_carmopolis = Vertex("Carmópolis", 14)
  vertex_cedro_de_sao_joao = Vertex("Cedro de São João", 15)
  vertex_cristinapolis = Vertex("Cristinápolis", 16)
  vertex_cumbe = Vertex("Cumbe", 17)
  vertex_divina_pastora = Vertex("Divina Pastora", 18)
  vertex_estancia = Vertex("Estância", 19)
  vertex_feira_nova = Vertex("Feira Nova", 20)
  vertex_frei_paulo = Vertex("Frei Paulo", 21)
  vertex_gararu = Vertex("Gararu", 22)
  vertex_general_maynard = Vertex("General Maynard", 23)
  vertex_gracho_cardoso = Vertex("Gracho Cardoso", 24)
  vertex_ilha_das_flores = Vertex("Ilha das Flores", 25)
  vertex_indiaroba = Vertex("Indiaroba", 26)
  vertex_itabaiana = Vertex("Itabaiana", 27)
  vertex_itabaianinha = Vertex("Itabaianinha", 28)
  vertex_itabi = Vertex("Itabi", 29)
  vertex_itaporanga_d_ajuda = Vertex("Itaporanga d’Ajuda", 30)
  vertex_japaratuba = Vertex("Japaratuba", 31)
  vertex_japoata = Vertex("Japoatã", 32)
  vertex_lagarto = Vertex("Lagarto", 33)
  vertex_laranjeiras = Vertex("Laranjeiras", 34)
  vertex_macambira = Vertex("Macambira", 35)
  vertex_malhada_dos_bois = Vertex("Malhada dos Bois", 36)
  vertex_malhador = Vertex("Malhador", 37)
  vertex_maruim = Vertex("Maruim", 38)
  vertex_moita_bonita = Vertex("Moita Bonita", 39)
  vertex_monte_alegre_de_sergipe = Vertex("Monte Alegre de Sergipe", 40)
  vertex_muribeca = Vertex("Muribeca", 41)
  vertex_neopolis = Vertex("Neópolis", 42)
  vertex_nossa_senhora_aparecida = Vertex("Nossa Senhora Aparecida", 43)
  vertex_nossa_senhora_da_gloria = Vertex("Nossa Senhora da Glória", 44)
  vertex_nossa_senhora_das_dores = Vertex("Nossa Senhora das Dores", 45)
  vertex_nossa_senhora_de_lourdes = Vertex("Nossa Senhora de Lourdes", 46)
  vertex_nossa_senhora_do_socorro = Vertex("Nossa Senhora do Socorro", 47)
  vertex_pacatuba = Vertex("Pacatuba", 48)
  vertex_pedra_mole = Vertex("Pedra Mole", 49)
  vertex_pedrinhas = Vertex("Pedrinhas", 50)
  vertex_pinhao = Vertex("Pinhão", 51)
  vertex_pirambu = Vertex("Pirambu", 52)
  vertex_porto_da_folha = Vertex("Porto da Folha", 53)
  vertex_poco_redondo = Vertex("Poço Redondo", 54)
  vertex_poco_verde = Vertex("Poço Verde", 55)
  vertex_propria = Vertex("Propriá", 56)
  vertex_riachuelo = Vertex("Riachuelo", 57)
  vertex_riachao_do_dantas = Vertex("Riachão do Dantas", 58)
  vertex_ribeiropolis = Vertex("Ribeirópolis", 59)
  vertex_rosario_do_catete = Vertex("Rosário do Catete", 60)
  vertex_salgado = Vertex("Salgado", 61)
  vertex_santa_luzia_do_itanhy = Vertex("Santa Luzia do Itanhy", 62)
  vertex_santa_rosa_de_lima = Vertex("Santa Rosa de Lima", 63)
  vertex_santana_do_sao_francisco = Vertex("Santana do São Francisco", 64)
  vertex_santo_amaro_das_brotas = Vertex("Santo Amaro das Brotas", 65)
  vertex_simao_dias = Vertex("Simão Dias", 66)
  vertex_siriri = Vertex("Siriri", 67)
  vertex_sao_cristovao = Vertex("São Cristóvão", 68)
  vertex_sao_domingos = Vertex("São Domingos", 69)
  vertex_sao_francisco = Vertex("São Francisco", 70)
  vertex_sao_miguel_do_aleixo = Vertex("São Miguel do Aleixo", 71)
  vertex_telha = Vertex("Telha", 72)
  vertex_tobias_barreto = Vertex("Tobias Barreto", 73)
  vertex_tomar_do_geru = Vertex("Tomar do Geru", 74)
  vertex_umbauba = Vertex("Umbaúba", 75)


  # Vizinhos Amparo de São Francisco
  
  edge_amparo_telha = Edge(vertex_amparo_de_sao_francisco, vertex_telha, 15.3)
  edge_amparo_canhoba = Edge(vertex_amparo_de_sao_francisco, vertex_canhoba, 9.6)
  edge_amparo_propria = Edge(vertex_amparo_de_sao_francisco, vertex_propria, 19,3)
  
  graph_citys_sergipe.add_edge(edge_amparo_telha)
  graph_citys_sergipe.add_edge(edge_amparo_canhoba)
  graph_citys_sergipe.add_edge(edge_amparo_propria)
  
  # Vizinhos Aquidabã
  
  edge_aquidaba_capela = Edge(vertex_aquidaba, vertex_capela, 46.3)
  edge_aquidaba_cumbe = Edge(vertex_aquidaba, vertex_cumbe, 24.3)
  edge_aquidaba_cedro = Edge(vertex_aquidaba, vertex_cedro_de_sao_joao, 21.7)
  edge_aquidaba_canhoba = Edge(vertex_aquidaba, vertex_canhoba, 22.5)
  edge_aquidaba_gracho = Edge(vertex_aquidaba, vertex_gracho_cardoso, 23.3)
  edge_aquidaba_muribeca = Edge(vertex_aquidaba, vertex_muribeca, 21.8)
  
  graph_citys_sergipe.add_edge(edge_aquidaba_capela)
  graph_citys_sergipe.add_edge(edge_aquidaba_cumbe)
  graph_citys_sergipe.add_edge(edge_aquidaba_cedro)
  graph_citys_sergipe.add_edge(edge_aquidaba_canhoba)
  graph_citys_sergipe.add_edge(edge_aquidaba_gracho)
  graph_citys_sergipe.add_edge(edge_aquidaba_muribeca)
  
  # Vizinhos Aracaju
  
  edge_aracaju_areia_branca = Edge(vertex_aracaju, vertex_areia_branca, 37.2)
  edge_aracaju_barra_dos_coqueiros = Edge(vertex_aracaju, vertex_barra_dos_coqueiros, 8.9)
  edge_aracaju_itaporanga = Edge(vertex_aracaju, vertex_itaporanga_d_ajuda, 33.3)
  edge_aracaju_laranjeiras = Edge(vertex_aracaju, vertex_laranjeiras, 22.5)
  edge_aracaju_socorro = Edge(vertex_aracaju, vertex_nossa_senhora_do_socorro, 16)
  edge_aracaju_sao_cristovao = Edge(vertex_aracaju, vertex_sao_cristovao, 22.9)
  
  graph_citys_sergipe.add_edge(edge_aracaju_areia_branca)
  graph_citys_sergipe.add_edge(edge_aracaju_barra_dos_coqueiros)
  graph_citys_sergipe.add_edge(edge_aracaju_itaporanga)
  graph_citys_sergipe.add_edge(edge_aracaju_laranjeiras)
  graph_citys_sergipe.add_edge(edge_aracaju_sao_cristovao)
  graph_citys_sergipe.add_edge(edge_aracaju_socorro)


  # Vizinhos Arauá

  edge_arua_estancia = Edge(vertex_araua, vertex_estancia, 32.9)
  edge_arua_itabaianinha = Edge(vertex_araua, vertex_pedrinhas, 21.4)
  edge_arua_pedrinhas = Edge(vertex_araua, vertex_pedrinhas, 10)
  edge_arua_umbauba = Edge(vertex_araua, vertex_umbauba, 18.5)

  graph_citys_sergipe.add_edge(edge_arua_estancia)
  graph_citys_sergipe.add_edge(edge_arua_pedrinhas)
  graph_citys_sergipe.add_edge(edge_arua_itabaianinha)
  graph_citys_sergipe.add_edge(edge_arua_umbauba)

  # Vizinhos Areia Branca

  edge_areia_branca_itabaiana = Edge(vertex_areia_branca, vertex_itabaiana, 18.7)
  edge_areia_branca_laranjeiras = Edge(vertex_areia_branca, vertex_laranjeiras, 24.1)
  edge_areia_branca_riachuelo = Edge(vertex_areia_branca, vertex_riachuelo, 21.6)
  edge_areia_branca_socorro = Edge(vertex_areia_branca, vertex_nossa_senhora_do_socorro, 31.2)

  graph_citys_sergipe.add_edge(edge_areia_branca_itabaiana)
  graph_citys_sergipe.add_edge(edge_areia_branca_laranjeiras)
  graph_citys_sergipe.add_edge(edge_areia_branca_riachuelo)
  graph_citys_sergipe.add_edge(edge_areia_branca_socorro)