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

  # Vizinhos Barra dos Coqueiros

  edge_barra_coqueiros_santo_amaro = Edge(vertex_barra_dos_coqueiros, vertex_santo_amaro_das_brotas, 33.3)
  edge_barra_coqueiros_pirambu = Edge(vertex_barra_dos_coqueiros, vertex_pirambu, 29.7)

  graph_citys_sergipe.add_edge(edge_barra_coqueiros_santo_amaro)
  graph_citys_sergipe.add_edge(edge_barra_coqueiros_pirambu)

  # Vizinhos Boquim

  edge_boquim_estancia = Edge(vertex_boquim, vertex_estancia, 27.3)
  edge_boquim_lagarto = Edge(vertex_boquim, vertex_lagarto, 38.3)
  edge_boquim_pedrinhas = Edge(vertex_boquim, vertex_pedrinhas, 7.9)
  edge_boquim_salgado = Edge(vertex_boquim, vertex_salgado, 24.2)

  graph_citys_sergipe.add_edge(edge_boquim_estancia)
  graph_citys_sergipe.add_edge(edge_boquim_lagarto)
  graph_citys_sergipe.add_edge(edge_boquim_pedrinhas)
  graph_citys_sergipe.add_edge(edge_boquim_salgado)

  # Vizinhos Brejo Grande

  edge_brejo_grande_ilha_das_flores = Edge(vertex_brejo_grande, vertex_ilha_das_flores, 9.3)
  edge_brejo_grande_pacatuba = Edge(vertex_brejo_grande, vertex_pacatuba, 26.2)
  edge_brejo_grande_pirambu = Edge(vertex_brejo_grande, vertex_pirambu, 70.5)

  graph_citys_sergipe.add_edge(edge_brejo_grande_ilha_das_flores)
  graph_citys_sergipe.add_edge(edge_brejo_grande_pacatuba)
  graph_citys_sergipe.add_edge(edge_brejo_grande_pirambu)

  # Vizinhos Campo do Brito

  edge_campo_do_brito_itabaiana = Edge(vertex_campo_do_brito, vertex_itabaiana, 11.7)
  edge_campo_do_brito_sao_domingos = Edge(vertex_campo_do_brito, vertex_sao_domingos, 11.9)

  graph_citys_sergipe.add_edge(edge_campo_do_brito_itabaiana)
  graph_citys_sergipe.add_edge(edge_campo_do_brito_sao_domingos)

  # Vizinhos Canhoba

  edge_canhoba_nossa_senhora_de_lourdes = Edge(vertex_canhoba, vertex_nossa_senhora_de_lourdes, 14.3)
  edge_canhoba_telha = Edge(vertex_canhoba, vertex_telha, 17.1)

  graph_citys_sergipe.add_edge(edge_canhoba_nossa_senhora_de_lourdes)
  graph_citys_sergipe.add_edge(edge_canhoba_telha)

  # Vizinhos Canindé de São Fransisco

  edge_caninde_sao_francisco_poco_redondo = Edge(vertex_caninde_de_sao_francisco, vertex_poco_redondo, 20.9)

  graph_citys_sergipe.add_edge(edge_caninde_sao_francisco_poco_redondo)

  # Vizinhos Capela

  edge_capela_carmopolis = Edge(vertex_capela, vertex_carmopolis, 26.1)
  edge_capela_japaratuba = Edge(vertex_capela, vertex_japaratuba, 24.1)
  edge_capela_muribeca = Edge(vertex_capela, vertex_muribeca, 22.2)
  edge_capela_nossa_senhora_das_dores = Edge(vertex_capela, vertex_nossa_senhora_das_dores, 19.4)
  edge_capela_siriri = Edge(vertex_capela, vertex_siriri, 14.7)
  edge_capela_rosario_do_catete = Edge(vertex_capela, vertex_rosario_do_catete, 32.7)

  graph_citys_sergipe.add_edge(edge_capela_carmopolis)
  graph_citys_sergipe.add_edge(edge_capela_japaratuba)
  graph_citys_sergipe.add_edge(edge_capela_nossa_senhora_das_dores)
  graph_citys_sergipe.add_edge(edge_capela_muribeca)
  graph_citys_sergipe.add_edge(edge_capela_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_capela_siriri)

  # Vizinhos Carira

  edge_carira_frei_paulo = Edge(vertex_carira, vertex_frei_paulo, 36.5)
  edge_carira_monte_alegre_de_sergipe = Edge(vertex_carira, vertex_monte_alegre_de_sergipe, 60)
  edge_carira_nossa_senhora_da_gloria = Edge(vertex_carira, vertex_nossa_senhora_da_gloria, 48)
  edge_carira_nossa_senhora_aparecida = Edge(vertex_carira, vertex_nossa_senhora_aparecida, 36.9)
  edge_carira_pinhao = Edge(vertex_carira, vertex_pinhao, 32.4)

  graph_citys_sergipe.add_edge(edge_carira_frei_paulo)
  graph_citys_sergipe.add_edge(edge_carira_monte_alegre_de_sergipe)
  graph_citys_sergipe.add_edge(edge_carira_nossa_senhora_da_gloria)
  graph_citys_sergipe.add_edge(edge_carira_nossa_senhora_aparecida)
  graph_citys_sergipe.add_edge(edge_carira_pinhao)

  # Vizinhos Carmópolis

  edge_carmopolis_aquidaba = Edge(vertex_carmopolis, vertex_aquidaba, 57.1)
  edge_carmopolis_general_maynard = Edge(vertex_carmopolis, vertex_general_maynard, 5.3)
  edge_carmopolis_japaratuba = Edge(vertex_carmopolis, vertex_japaratuba, 12.9)
  edge_carmopolis_japoata = Edge(vertex_carmopolis, vertex_japoata, 50.1)
  edge_carmopolis_muribeca = Edge(vertex_carmopolis, vertex_muribeca, 37.4)
  edge_carmopolis_pirambu = Edge(vertex_carmopolis, vertex_pirambu, 30)
  edge_carmopolis_rosario_do_catete = Edge(vertex_carmopolis, vertex_rosario_do_catete , 12.8)
  edge_carmopolis_siriri = Edge(vertex_carmopolis, vertex_siriri, 19.2)
  edge_carmopolis_sao_francisco = Edge(vertex_carmopolis, vertex_sao_francisco, 40.8)

  graph_citys_sergipe.add_edge(edge_carmopolis_aquidaba)
  graph_citys_sergipe.add_edge(edge_carmopolis_general_maynard)
  graph_citys_sergipe.add_edge(edge_carmopolis_japaratuba)
  graph_citys_sergipe.add_edge(edge_carmopolis_japoata)
  graph_citys_sergipe.add_edge(edge_carmopolis_muribeca)
  graph_citys_sergipe.add_edge(edge_carmopolis_pirambu)
  graph_citys_sergipe.add_edge(edge_carmopolis_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_carmopolis_siriri)
  graph_citys_sergipe.add_edge(edge_carmopolis_sao_francisco)

  # Vizinhos Cedro de São João

  edge_cedro_sao_joao_japoata = Edge(vertex_cedro_de_sao_joao, vertex_japoata, 17.3)
  edge_cedro_sao_joao_muribeca = Edge(vertex_cedro_de_sao_joao, vertex_muribeca, 26.4)
  edge_cedro_sao_joao_propria = Edge(vertex_cedro_de_sao_joao, vertex_propria, 11.8)
  edge_cedro_sao_joao_telha = Edge(vertex_cedro_de_sao_joao, vertex_telha, 5.8)

  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_japoata)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_muribeca)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_telha)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_propria)

  # Vizinhos Cristinápolis

  edge_cristinapolis_indiaroba = Edge(vertex_cristinapolis, vertex_indiaroba, 45.6)
  edge_cristinapolis_tomar_do_geru = Edge(vertex_cristinapolis, vertex_tomar_do_geru, 17.1)
  edge_cristinapolis_umbauba = Edge(vertex_cristinapolis, vertex_umbauba, 16.5)

  graph_citys_sergipe.add_edge(edge_cristinapolis_indiaroba)
  graph_citys_sergipe.add_edge(edge_cristinapolis_tomar_do_geru)
  graph_citys_sergipe.add_edge(edge_cristinapolis_umbauba)

  # Vizinhos Cumbe

  edge_cumbe_itabi = Edge(vertex_cumbe, vertex_itabi, 34.1)
  edge_cumbe_feira_nova = Edge(vertex_cumbe, vertex_feira_nova, 25.5)
  edge_cumbe_nossa_senhora_das_dores = Edge(vertex_cumbe, vertex_nossa_senhora_das_dores, 18.3)
  edge_cumbe_sao_miguel_do_aleixo = Edge(vertex_cumbe, vertex_sao_miguel_do_aleixo, 30.1)

  graph_citys_sergipe.add_edge(edge_cumbe_feira_nova)
  graph_citys_sergipe.add_edge(edge_cumbe_itabi)
  graph_citys_sergipe.add_edge(edge_cumbe_nossa_senhora_das_dores)
  graph_citys_sergipe.add_edge(edge_cumbe_sao_miguel_do_aleixo)