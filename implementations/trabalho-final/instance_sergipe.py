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
  edge_aquidaba_japaratuba = Edge(vertex_aquidaba, vertex_japaratuba, 50.2)
  edge_aquidaba_japoata = Edge(vertex_aquidaba, vertex_japoata, 38.5)
  edge_aquidaba_malhada_dos_bois = Edge(vertex_aquidaba, vertex_malhada_dos_bois, 27.5)
  
  graph_citys_sergipe.add_edge(edge_aquidaba_capela)
  graph_citys_sergipe.add_edge(edge_aquidaba_cumbe)
  graph_citys_sergipe.add_edge(edge_aquidaba_cedro)
  graph_citys_sergipe.add_edge(edge_aquidaba_canhoba)
  graph_citys_sergipe.add_edge(edge_aquidaba_gracho)
  graph_citys_sergipe.add_edge(edge_aquidaba_muribeca)
  graph_citys_sergipe.add_edge(edge_aquidaba_japaratuba)
  graph_citys_sergipe.add_edge(edge_aquidaba_japoata)
  graph_citys_sergipe.add_edge(edge_aquidaba_malhada_dos_bois)
  
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
  edge_arua_itabaianinha = Edge(vertex_araua, vertex_itabaianinha, 21.4)
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
  edge_canhoba_propria = Edge(vertex_canhoba, vertex_propria, 21.5)

  graph_citys_sergipe.add_edge(edge_canhoba_nossa_senhora_de_lourdes)
  graph_citys_sergipe.add_edge(edge_canhoba_telha)
  graph_citys_sergipe.add_edge(edge_canhoba_propria)

  # Vizinhos Canindé de São Fransisco

  edge_caninde_sao_francisco_poco_redondo = Edge(vertex_caninde_de_sao_francisco, vertex_poco_redondo, 20.9)
  edge_caninde_de_sao_francisco_monte_alegre_de_Sergipe = Edge(vertex_caninde_de_sao_francisco, vertex_monte_alegre_de_sergipe, 100) #passando por pelado
  
  graph_citys_sergipe.add_edge(edge_caninde_sao_francisco_poco_redondo)
  graph_citys_sergipe.add_edge(edge_caninde_de_sao_francisco_monte_alegre_de_Sergipe)

  # Vizinhos Capela

  edge_capela_carmopolis = Edge(vertex_capela, vertex_carmopolis, 26.1)
  edge_capela_japaratuba = Edge(vertex_capela, vertex_japaratuba, 24.1)
  edge_capela_muribeca = Edge(vertex_capela, vertex_muribeca, 22.2)
  edge_capela_nossa_senhora_das_dores = Edge(vertex_capela, vertex_nossa_senhora_das_dores, 19.4)
  edge_capela_siriri = Edge(vertex_capela, vertex_siriri, 14.7)
  edge_capela_rosario_do_catete = Edge(vertex_capela, vertex_rosario_do_catete, 32.7)
  edge_capela_malhada_dos_bois = Edge(vertex_capela, vertex_malhada_dos_bois, 31.8)

  graph_citys_sergipe.add_edge(edge_capela_carmopolis)
  graph_citys_sergipe.add_edge(edge_capela_japaratuba)
  graph_citys_sergipe.add_edge(edge_capela_nossa_senhora_das_dores)
  graph_citys_sergipe.add_edge(edge_capela_muribeca)
  graph_citys_sergipe.add_edge(edge_capela_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_capela_siriri)
  graph_citys_sergipe.add_edge(edge_capela_malhada_dos_bois)

  # Vizinhos Carira

  edge_carira_frei_paulo = Edge(vertex_carira, vertex_frei_paulo, 36.5)
  edge_carira_monte_alegre_de_sergipe = Edge(vertex_carira, vertex_monte_alegre_de_sergipe, 60)
  edge_carira_nossa_senhora_da_gloria = Edge(vertex_carira, vertex_nossa_senhora_da_gloria, 48)
  edge_carira_nossa_senhora_aparecida = Edge(vertex_carira, vertex_nossa_senhora_aparecida, 36.9)
  edge_carira_pinhao = Edge(vertex_carira, vertex_pinhao, 32.4)
  edge_carira_pedra_mole = Edge(vertex_carira, vertex_pedra_mole, 35.9)

  graph_citys_sergipe.add_edge(edge_carira_frei_paulo)
  graph_citys_sergipe.add_edge(edge_carira_monte_alegre_de_sergipe)
  graph_citys_sergipe.add_edge(edge_carira_nossa_senhora_da_gloria)
  graph_citys_sergipe.add_edge(edge_carira_nossa_senhora_aparecida)
  graph_citys_sergipe.add_edge(edge_carira_pinhao)
  graph_citys_sergipe.add_edge(edge_carira_pedra_mole)

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
  edge_carmopolis_malhada_dos_bois = Edge(vertex_carmopolis, vertex_malhada_dos_bois, 39.9)

  graph_citys_sergipe.add_edge(edge_carmopolis_aquidaba)
  graph_citys_sergipe.add_edge(edge_carmopolis_general_maynard)
  graph_citys_sergipe.add_edge(edge_carmopolis_japaratuba)
  graph_citys_sergipe.add_edge(edge_carmopolis_japoata)
  graph_citys_sergipe.add_edge(edge_carmopolis_muribeca)
  graph_citys_sergipe.add_edge(edge_carmopolis_pirambu)
  graph_citys_sergipe.add_edge(edge_carmopolis_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_carmopolis_siriri)
  graph_citys_sergipe.add_edge(edge_carmopolis_sao_francisco)
  graph_citys_sergipe.add_edge(edge_carmopolis_malhada_dos_bois)

  # Vizinhos Cedro de São João

  edge_cedro_sao_joao_japoata = Edge(vertex_cedro_de_sao_joao, vertex_japoata, 17.3)
  edge_cedro_sao_joao_muribeca = Edge(vertex_cedro_de_sao_joao, vertex_muribeca, 26.4)
  edge_cedro_sao_joao_sao_francisco = Edge(vertex_cedro_de_sao_joao, vertex_sao_francisco, 15.6)
  edge_cedro_sao_joao_propria = Edge(vertex_cedro_de_sao_joao, vertex_propria, 11.8)
  edge_cedro_sao_joao_telha = Edge(vertex_cedro_de_sao_joao, vertex_telha, 5.8)
  edge_cedro_sao_joao_malhada_dos_bois = Edge(vertex_cedro_de_sao_joao, vertex_malhada_dos_bois, 19.2)

  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_japoata)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_muribeca)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_telha)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_sao_francisco)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_propria)
  graph_citys_sergipe.add_edge(edge_cedro_sao_joao_malhada_dos_bois)

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
  
  # Vizinhos Divina Pastora
  
  edge_divina_pastora_riachuelo = Edge(vertex_divina_pastora, vertex_riachuelo, 9.5)
  edge_divina_pastora_santa_rosa_de_lima = Edge(vertex_divina_pastora, vertex_santa_rosa_de_lima, 10.4)
  edge_divina_pastora_siriri = Edge(vertex_divina_pastora, vertex_siriri, 10.9)
  edge_divina_pastora_malhador = Edge(vertex_divina_pastora, vertex_malhador, 27)
  
  graph_citys_sergipe.add_edge(edge_divina_pastora_riachuelo)
  graph_citys_sergipe.add_edge(edge_divina_pastora_santa_rosa_de_lima)
  graph_citys_sergipe.add_edge(edge_divina_pastora_siriri)
  graph_citys_sergipe.add_edge(edge_divina_pastora_malhador)
  
  # Vizinhos Estancia
  
  edge_estancia_santa_luiza_do_itanhy = Edge(vertex_estancia, vertex_santa_luzia_do_itanhy, 10.8)
  edge_estancia_umabuba = Edge(vertex_estancia, vertex_umbauba, 32.1)
  edge_estancia_salgado = Edge(vertex_estancia, vertex_salgado, 42.1)
  edge_estancia_itaporanga_d_ajuda = Edge(vertex_estancia, vertex_itaporanga_d_ajuda, 38.6)
  
  graph_citys_sergipe.add_edge(edge_estancia_santa_luiza_do_itanhy)
  graph_citys_sergipe.add_edge(edge_estancia_itaporanga_d_ajuda)
  graph_citys_sergipe.add_edge(edge_estancia_umabuba)
  graph_citys_sergipe.add_edge(edge_estancia_salgado)
  
  # Vizinhos Feira Nova
  
  edge_feira_nova_graccho = Edge(vertex_feira_nova, vertex_gracho_cardoso, 14.4)
  edge_feira_nova_nossa_s_gloria = Edge(vertex_feira_nova, vertex_nossa_senhora_da_gloria, 14.1)
  edge_feira_nova_nossa_s_dores = Edge(vertex_feira_nova, vertex_nossa_senhora_das_dores, 32)
  edge_feira_nova_sao_miguel_aleixo = Edge(vertex_feira_nova, vertex_sao_miguel_do_aleixo, 20)
  
  graph_citys_sergipe.add_edge(edge_feira_nova_nossa_s_dores)
  graph_citys_sergipe.add_edge(edge_feira_nova_graccho)
  graph_citys_sergipe.add_edge(edge_feira_nova_nossa_s_gloria)
  graph_citys_sergipe.add_edge(edge_feira_nova_sao_miguel_aleixo)
  
  # Vizinhos Frei Paulo
  
  edge_frei_paulo_ribeiropolis = Edge(vertex_frei_paulo, vertex_ribeiropolis, 18.7)
  edge_frei_paulo_pinhao = Edge(vertex_frei_paulo, vertex_pinhao, 22.7)
  edge_frei_paulo_nossa_s_aparecida = Edge(vertex_frei_paulo, vertex_nossa_senhora_aparecida, 21.1)
  edge_frei_paulo_pedra_mole = Edge(vertex_frei_paulo, vertex_pedra_mole, 22)
  edge_frei_paulo_itabaiana = Edge(vertex_frei_paulo, vertex_itabaiana, 20.2)
  
  graph_citys_sergipe.add_edge(edge_frei_paulo_ribeiropolis)
  graph_citys_sergipe.add_edge(edge_frei_paulo_pinhao)
  graph_citys_sergipe.add_edge(edge_frei_paulo_nossa_s_aparecida)
  graph_citys_sergipe.add_edge(edge_frei_paulo_pedra_mole)
  graph_citys_sergipe.add_edge(edge_frei_paulo_itabaiana)
  
  # Vizinhos Gararu
  
  edge_gararu_itabi = Edge(vertex_gararu, vertex_itabi, 23.3)
  edge_gararu_porto_da_folha = Edge(vertex_gararu, vertex_porto_da_folha, 26.4)
  edge_gararu_nossa_senhora_de_lourdes = Edge(vertex_gararu, vertex_nossa_senhora_de_lourdes, 19.4)
  edge_gararu_nossa_senhora_da_gloria = Edge(vertex_gararu, vertex_nossa_senhora_da_gloria, 66.4)
  
  graph_citys_sergipe.add_edge(edge_gararu_itabi)
  graph_citys_sergipe.add_edge(edge_gararu_porto_da_folha)
  graph_citys_sergipe.add_edge(edge_gararu_nossa_senhora_de_lourdes)
  graph_citys_sergipe.add_edge(edge_gararu_nossa_senhora_da_gloria)
  
  # Vizinhos General Maynard
  
  edge_general_maynard_rosario_do_catete = Edge(vertex_general_maynard, vertex_rosario_do_catete, 6.6)
  
  graph_citys_sergipe.add_edge(edge_general_maynard_rosario_do_catete)
  
  # Vizinhos Gracho Cardoso
  
  edge_graccho_itabi = Edge(vertex_gracho_cardoso, vertex_itabi, 18.6)
  
  graph_citys_sergipe.add_edge(edge_graccho_itabi)
  
  # Vizinhos Ilha das Flores
  
  edge_ilha_das_flores_brejo_grande = Edge(vertex_ilha_das_flores, vertex_brejo_grande, 9.3)
  edge_ilha_das_flores_pacatuba = Edge(vertex_ilha_das_flores, vertex_pacatuba, 23)
  edge_ilha_das_flores_neopolis = Edge(vertex_ilha_das_flores, vertex_neopolis, 17)
  edge_ilha_das_flores_japaratuba = Edge(vertex_ilha_das_flores, vertex_japaratuba, 67.4)
  
  graph_citys_sergipe.add_edge(edge_ilha_das_flores_brejo_grande)
  graph_citys_sergipe.add_edge(edge_ilha_das_flores_pacatuba)
  graph_citys_sergipe.add_edge(edge_ilha_das_flores_neopolis)
  graph_citys_sergipe.add_edge(edge_ilha_das_flores_japaratuba)

  # Vizinhos Indiabora

  edge_indiabora_santa_luzia_do_itanhy = Edge(vertex_indiaroba, vertex_santa_luzia_do_itanhy, 22.6)
  edge_indiabora_umbauba = Edge(vertex_indiaroba, vertex_umbauba, 25.9)
  
  graph_citys_sergipe.add_edge(edge_indiabora_santa_luzia_do_itanhy)
  graph_citys_sergipe.add_edge(edge_indiabora_umbauba)
    
  
  # Vizinhos Itabaiana
  
  edge_itabaiana_malhador = Edge(vertex_itabaiana, vertex_malhador, 18)
  edge_itabaiana_moita_bonita = Edge(vertex_itabaiana, vertex_moita_bonita, 16.6)
  edge_itabaiana_ribeiropolis = Edge(vertex_itabaiana, vertex_ribeiropolis, 21.5)
  edge_itabaiana_macambira = Edge(vertex_itabaiana, vertex_macambira, 14.2)
  
  graph_citys_sergipe.add_edge(edge_itabaiana_malhador)
  graph_citys_sergipe.add_edge(edge_itabaiana_moita_bonita)
  graph_citys_sergipe.add_edge(edge_itabaiana_ribeiropolis)
  graph_citys_sergipe.add_edge(edge_itabaiana_macambira)

  # Vizinhos Itabaianinha

  edge_itabaianinha_tomar_do_geru = Edge(vertex_itabaianinha, vertex_tomar_do_geru, 19.1)
  edge_itabaianinha_umbauba = Edge(vertex_itabaianinha, vertex_umbauba, 20.5)
  edge_itabaianinha_tobias_barreto = Edge(vertex_itabaianinha, vertex_tobias_barreto, 30.8)

  graph_citys_sergipe.add_edge(edge_itabaianinha_tomar_do_geru)
  graph_citys_sergipe.add_edge(edge_itabaianinha_umbauba)
  graph_citys_sergipe.add_edge(edge_itabaianinha_tobias_barreto)

  # Vizinhos Itabi

  edge_itabi_nossa_senhora_de_lourdes = Edge(vertex_itabi, vertex_nossa_senhora_de_lourdes, 12.2)

  graph_citys_sergipe.add_edge(edge_itabi_nossa_senhora_de_lourdes)

  # Vizinhos Itaporanga d'Ajuda

  edge_itaporanga_d_ajuda_salgado = Edge(vertex_itaporanga_d_ajuda, vertex_salgado, 22.6)
  edge_itaporanga_d_ajuda_lagarto = Edge(vertex_itaporanga_d_ajuda, vertex_lagarto, 46.2)
  edge_itaporanga_d_ajuda_sao_cristovao = Edge(vertex_itaporanga_d_ajuda, vertex_sao_cristovao, 15.6)
  edge_itaporanga_d_ajuda_nossa_senhora_do_socorro = Edge(vertex_itaporanga_d_ajuda, vertex_nossa_senhora_do_socorro, 31.5)

  graph_citys_sergipe.add_edge(edge_itaporanga_d_ajuda_salgado)
  graph_citys_sergipe.add_edge(edge_itaporanga_d_ajuda_lagarto)
  graph_citys_sergipe.add_edge(edge_itaporanga_d_ajuda_sao_cristovao)
  graph_citys_sergipe.add_edge(edge_itaporanga_d_ajuda_nossa_senhora_do_socorro)

  # Vizinhos Japaratuba

  edge_japaratuba_muribeca = Edge(vertex_japaratuba, vertex_muribeca, 31)
  edge_japaratuba_sao_francisco = Edge(vertex_japaratuba, vertex_sao_francisco, 33.9)
  edge_japaratuba_pirambu = Edge(vertex_japaratuba, vertex_pirambu, 21.5)
  edge_japaratuba_pacatuba = Edge(vertex_japaratuba, vertex_pacatuba, 60.4)
  edge_japaratuba_rosario_do_catete = Edge(vertex_japaratuba, vertex_rosario_do_catete, 22.3)
  edge_japaratuba_siriri = Edge(vertex_japaratuba, vertex_siriri, 29.1)
  edge_japaratuba_japoata = Edge(vertex_japaratuba, vertex_japoata, 43.2)
  edge_japaratuba_malhada_dos_bois = Edge(vertex_japaratuba, vertex_malhada_dos_bois, 37)

  graph_citys_sergipe.add_edge(edge_japaratuba_muribeca)
  graph_citys_sergipe.add_edge(edge_japaratuba_sao_francisco)
  graph_citys_sergipe.add_edge(edge_japaratuba_pirambu)
  graph_citys_sergipe.add_edge(edge_japaratuba_pacatuba)
  graph_citys_sergipe.add_edge(edge_japaratuba_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_japaratuba_siriri)
  graph_citys_sergipe.add_edge(edge_japaratuba_japoata)
  graph_citys_sergipe.add_edge(edge_japaratuba_malhada_dos_bois)

  # Vizinhos Japoatã

  edge_japoata_propria = Edge(vertex_japoata, vertex_propria, 18)
  edge_japoata_neopolis = Edge(vertex_japoata, vertex_neopolis, 26.8)
  edge_japoata_pacatuba = Edge(vertex_japoata, vertex_pacatuba, 22)
  edge_japoata_malhada_dos_bois = Edge(vertex_japoata, vertex_malhada_dos_bois, 21.6)
  edge_japoata_muribeca = Edge(vertex_japoata, vertex_muribeca, 25.6)
  edge_japoata_santana_do_sao_francisco = Edge(vertex_japoata, vertex_santana_do_sao_francisco, 28.5)

  graph_citys_sergipe.add_edge(edge_japoata_propria)
  graph_citys_sergipe.add_edge(edge_japoata_neopolis)
  graph_citys_sergipe.add_edge(edge_japoata_pacatuba)
  graph_citys_sergipe.add_edge(edge_japoata_malhada_dos_bois)
  graph_citys_sergipe.add_edge(edge_japoata_muribeca)
  graph_citys_sergipe.add_edge(edge_japoata_santana_do_sao_francisco)

  # Vizinhos Lagarto

  edge_lagarto_simao_dias = Edge(vertex_lagarto, vertex_simao_dias, 26.5)
  edge_lagarto_riachao_do_dantas = Edge(vertex_lagarto, vertex_riachao_do_dantas, 20)
  edge_lagarto_sao_domingos = Edge(vertex_lagarto, vertex_sao_domingos, 21.7)
  edge_lagarto_salgado = Edge(vertex_lagarto, vertex_salgado, 25.5)

  graph_citys_sergipe.add_edge(edge_lagarto_simao_dias)
  graph_citys_sergipe.add_edge(edge_lagarto_riachao_do_dantas)
  graph_citys_sergipe.add_edge(edge_lagarto_sao_domingos)
  graph_citys_sergipe.add_edge(edge_lagarto_salgado)

  # Vizinhos Laranjeiras

  edge_laranjeiras_riachuelo = Edge(vertex_laranjeiras, vertex_riachuelo, 12.3)
  edge_laranjeiras_maruim = Edge(vertex_laranjeiras, vertex_maruim, 13.3)
  edge_laranjeiras_nossa_sra_socorro = Edge(vertex_laranjeiras, vertex_nossa_senhora_do_socorro, 9.1)

  graph_citys_sergipe.add_edge(edge_laranjeiras_riachuelo)
  graph_citys_sergipe.add_edge(edge_laranjeiras_maruim)
  graph_citys_sergipe.add_edge(edge_laranjeiras_nossa_sra_socorro)

  # Vizinhos Macambira

  edge_macambira_pinhao = Edge(vertex_macambira, vertex_pinhao, 26.1)
  edge_macambira_frei_paulo = Edge(vertex_macambira, vertex_frei_paulo, 22.9)
  edge_macambira_ribeiropolis = Edge(vertex_macambira, vertex_ribeiropolis, 24)
  edge_macambira_carira = Edge(vertex_macambira, vertex_carira, 48)
  edge_macambira_nossa_senhora_da_gloria = Edge(vertex_macambira, vertex_nossa_senhora_da_gloria, 99.6)
  edge_macambira_pedra_mole = Edge(vertex_macambira, vertex_pedra_mole, 21.3)

  graph_citys_sergipe.add_edge(edge_macambira_pinhao)
  graph_citys_sergipe.add_edge(edge_macambira_frei_paulo)
  graph_citys_sergipe.add_edge(edge_macambira_ribeiropolis)
  graph_citys_sergipe.add_edge(edge_macambira_carira)
  graph_citys_sergipe.add_edge(edge_macambira_nossa_senhora_da_gloria)
  graph_citys_sergipe.add_edge(edge_macambira_pedra_mole)

  # Vizinhos Malhada dos Bois

  edge_malhada_dos_bois_sao_francisco = Edge(vertex_malhada_dos_bois, vertex_sao_francisco, 7.1)
  edge_malhada_dos_bois_propria = Edge(vertex_malhada_dos_bois, vertex_propria, 23)
  edge_malhada_dos_bois_rosario_do_catete = Edge(vertex_malhada_dos_bois, vertex_rosario_do_catete, 46.5)
  edge_malhada_dos_bois_muribeca = Edge(vertex_malhada_dos_bois, vertex_muribeca, 12.2)

  graph_citys_sergipe.add_edge(edge_malhada_dos_bois_sao_francisco)
  graph_citys_sergipe.add_edge(edge_malhada_dos_bois_propria)
  graph_citys_sergipe.add_edge(edge_malhada_dos_bois_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_malhada_dos_bois_muribeca)
  
  # Vizinhos Malhador
  
  edge_malhador_riachuelo = Edge(vertex_malhador, vertex_riachuelo, 19.5)
  edge_malhador_moita_bonita = Edge(vertex_malhador, vertex_moita_bonita, 14.2)
  
  graph_citys_sergipe.add_edge(edge_malhador_riachuelo)
  graph_citys_sergipe.add_edge(edge_malhador_moita_bonita)
  
  # Vizinhos Maruim
  
  edge_maruim_santo_amaro_das_brotas = Edge(vertex_maruim, vertex_santo_amaro_das_brotas, 7.9)
  edge_maruim_rosario_do_catete = Edge(vertex_maruim, vertex_rosario_do_catete, 8)
  edge_maruim_nossa_senhora_do_socorro = Edge(vertex_maruim, vertex_nossa_senhora_do_socorro, 17.7)
  edge_maruim_pirambu = Edge(vertex_maruim, vertex_pirambu, 36.6)
  
  graph_citys_sergipe.add_edge(edge_maruim_santo_amaro_das_brotas)
  graph_citys_sergipe.add_edge(edge_maruim_rosario_do_catete)
  graph_citys_sergipe.add_edge(edge_maruim_nossa_senhora_do_socorro)
  graph_citys_sergipe.add_edge(edge_maruim_pirambu)
  
  # Vizinhos Moita Bonita
  
  edge_moita_bonita_ribeiropolis = Edge(vertex_moita_bonita, vertex_ribeiropolis, 12.1)
  edge_moita_bonita_nossa_s_das_dores = Edge(vertex_moita_bonita, vertex_nossa_senhora_das_dores, 25.6)
  edge_moita_bonita_santa_rosa_de_lima = Edge(vertex_moita_bonita, vertex_santa_rosa_de_lima, 22)
  edge_moita_bonita_sao_miguel_do_aleixo = Edge(vertex_moita_bonita, vertex_sao_miguel_do_aleixo, 27.7)
  
  graph_citys_sergipe.add_edge(edge_moita_bonita_nossa_s_das_dores)
  graph_citys_sergipe.add_edge(edge_moita_bonita_ribeiropolis)
  graph_citys_sergipe.add_edge(edge_moita_bonita_sao_miguel_do_aleixo)
  graph_citys_sergipe.add_edge(edge_moita_bonita_santa_rosa_de_lima)
  
  # Vizinhos Monte Alegre de Sergipe
  
  edge_monte_alegre_de_Sergipe_nossa_s_d_gloria = Edge(vertex_monte_alegre_de_sergipe, vertex_nossa_senhora_da_gloria, 28.2)
  edge_monte_alegre_de_Sergipe_porto_da_folha = Edge(vertex_monte_alegre_de_sergipe, vertex_porto_da_folha, 41.7)
  edge_monte_alegre_de_Sergipe_poco_redondo = Edge(vertex_monte_alegre_de_sergipe, vertex_poco_redondo, 29.2)
  
  graph_citys_sergipe.add_edge(edge_monte_alegre_de_Sergipe_poco_redondo)
  graph_citys_sergipe.add_edge(edge_monte_alegre_de_Sergipe_nossa_s_d_gloria)
  graph_citys_sergipe.add_edge(edge_monte_alegre_de_Sergipe_porto_da_folha)

  # Vizinhos Muribeca

  edge_muribeca_propria = Edge(vertex_muribeca, vertex_propria, 30.9)
  edge_muribeca_sao_francisco = Edge(vertex_muribeca, vertex_sao_francisco, 14.9)

  graph_citys_sergipe.add_edge(edge_muribeca_propria)
  graph_citys_sergipe.add_edge(edge_muribeca_sao_francisco)

  # Vizinhos Neópolis

  edge_neopolis_pacatuba = Edge(vertex_neopolis, vertex_pacatuba, 25.8)
  edge_neopolis_santana_do_sao_francisco = Edge(vertex_neopolis, vertex_santana_do_sao_francisco, 4.4)
  edge_neopolis_propria = Edge(vertex_neopolis, vertex_propria, 41)

  graph_citys_sergipe.add_edge(edge_neopolis_pacatuba)
  graph_citys_sergipe.add_edge(edge_neopolis_santana_do_sao_francisco)
  graph_citys_sergipe.add_edge(edge_neopolis_propria)

  # Vizinhos Nossa Senhora Aparecida

  edge_nossa_senhora_aparecida_nossa_senhora_da_gloria = Edge(vertex_nossa_senhora_aparecida, vertex_nossa_senhora_da_gloria, 22.8)
  edge_nossa_senhora_aparecida_sao_miguel_do_aleixo  = Edge(vertex_nossa_senhora_aparecida, vertex_sao_miguel_do_aleixo, 9)
  edge_nossa_senhora_aparecida_ribeiropolis  = Edge(vertex_nossa_senhora_aparecida, vertex_ribeiropolis, 18.2)

  graph_citys_sergipe.add_edge(edge_nossa_senhora_aparecida_nossa_senhora_da_gloria)
  graph_citys_sergipe.add_edge(edge_nossa_senhora_aparecida_sao_miguel_do_aleixo)
  graph_citys_sergipe.add_edge(edge_nossa_senhora_aparecida_ribeiropolis)

  # Vizinhos Nossa Senhora da Glória
  
  edge_nossa_senhora_da_gloria_porto_da_folha = Edge(vertex_nossa_senhora_da_gloria, vertex_porto_da_folha ,56.6)

  graph_citys_sergipe.add_edge(edge_nossa_senhora_da_gloria_porto_da_folha)

  # Vizinhos Nossa Senhora das Dores

  edge_nossa_senhora_das_dores_siriri = Edge(vertex_nossa_senhora_das_dores, vertex_siriri, 18)
  edge_nossa_senhora_das_dores_sao_miguel_do_aleixo = Edge(vertex_nossa_senhora_das_dores, vertex_sao_miguel_do_aleixo, 40)
  edge_nossa_senhora_das_dores_ribeiropolis = Edge(vertex_nossa_senhora_das_dores, vertex_ribeiropolis, 33.3)

  graph_citys_sergipe.add_edge(edge_nossa_senhora_das_dores_siriri)
  graph_citys_sergipe.add_edge(edge_nossa_senhora_das_dores_sao_miguel_do_aleixo)
  graph_citys_sergipe.add_edge(edge_nossa_senhora_das_dores_ribeiropolis)

  # Vizinhos Nossa Senhora de Lourdes

  # Vizinhos Nossa Senhora de Socorro

  # Vizinhos Pacatuba

  edge_pacatuba_pirambu = Edge(vertex_pacatuba, vertex_pirambu, 60.3)

  graph_citys_sergipe.add_edge(edge_pacatuba_pirambu)

  # Vizinhos Pedra Mole

  edge_pedra_mole_pinhao = Edge(vertex_pedra_mole, vertex_pinhao, 9.5)
  edge_pedra_mole_simao_dias = Edge(vertex_pedra_mole, vertex_simao_dias, 27)

  graph_citys_sergipe.add_edge(edge_pedra_mole_pinhao)
  graph_citys_sergipe.add_edge(edge_pedra_mole_simao_dias)

  # Vizinhos Pedrinhas

  edge_pedinhas_riachao_do_dantas = Edge(vertex_pedrinhas, vertex_riachao_do_dantas, 16.6)

  graph_citys_sergipe.add_edge(edge_pedinhas_riachao_do_dantas)

  # Vizinhos Pinhão

  edge_pinhao_simao_dias = Edge(vertex_pinhao, vertex_simao_dias, 24.4)

  graph_citys_sergipe.add_edge(edge_pinhao_simao_dias)

  # Vizinhos Pirambu

  edge_pirambu_santo_amaro_das_brotas = Edge(vertex_pirambu, vertex_santo_amaro_das_brotas, 35.7)

  graph_citys_sergipe.add_edge(edge_pirambu_santo_amaro_das_brotas)

  # Vizinhos Porto da Folha

  edge_porto_da_folha_poco_redondo = Edge(vertex_porto_da_folha, vertex_poco_redondo, 71.1)

  graph_citys_sergipe.add_edge(edge_porto_da_folha_poco_redondo)

  # Vizinhos Poço Redondo
  
  # Vizinhos Poço Verde

  edge_poco_verde_simao_dias = Edge(vertex_poco_verde, vertex_simao_dias, 44.9)
  edge_poco_verde_tobias_barreto = Edge(vertex_poco_verde, vertex_tobias_barreto, 56.3)

  graph_citys_sergipe.add_edge(edge_poco_verde_simao_dias)
  graph_citys_sergipe.add_edge(edge_poco_verde_tobias_barreto)

  # Vizinhos Propriá

  edge_propria_sao_fracisco = Edge(vertex_propria, vertex_sao_francisco, 22.5)
  edge_propria_telha = Edge(vertex_propria, vertex_telha, 9,4)
  edge_propria_sanatana_do_sao_fracisco = Edge(vertex_propria, vertex_santana_do_sao_francisco, 39.3)

  graph_citys_sergipe.add_edge(edge_propria_sao_fracisco)
  graph_citys_sergipe.add_edge(edge_propria_sanatana_do_sao_fracisco)
  graph_citys_sergipe.add_edge(edge_propria_telha)

  # Vizinhos Riachuelo

  edge_riachuelo_santa_rosa_de_lima = Edge(vertex_riachuelo, vertex_santa_rosa_de_lima, 11.5)

  graph_citys_sergipe.add_edge(edge_riachuelo_santa_rosa_de_lima)

  # Vizinhos Riachão do Dantas

  edge_riachao_tobias_barreto = Edge(vertex_riachao_do_dantas, vertex_tobias_barreto, 33.1)

  graph_citys_sergipe.add_edge(edge_riachao_tobias_barreto)
  
  # Vizinhos Ribeirópolis

  edge_ribeiropolis_sao_miguel_do_aleixo = Edge(vertex_ribeiropolis, vertex_sao_miguel_do_aleixo, 36.4)

  graph_citys_sergipe.add_edge(edge_ribeiropolis_sao_miguel_do_aleixo)

  # Vizinhos Rosário do Catete  
  
  edge_rosario_do_catete_santo_amaro_das_brotas = Edge(vertex_rosario_do_catete, vertex_santo_amaro_das_brotas, 15.9)
  edge_rosario_do_catete_siriri = Edge(vertex_rosario_do_catete, vertex_siriri, 17.2)
  
  graph_citys_sergipe.add_edge(edge_rosario_do_catete_siriri)
  graph_citys_sergipe.add_edge(edge_rosario_do_catete_santo_amaro_das_brotas)
  
  # Vizinhos Salgado  
  
  edge_salgado_sao_domingos = Edge(vertex_salgado, vertex_sao_domingos, 40.3)
  
  graph_citys_sergipe.add_edge(edge_salgado_sao_domingos)  
  
  # Vizinhos Santa Luiza do Itanhy
  
  # Vizinhos Santa Rosa De lima
  
  # Vizinhos Santana do São Francisco
  
  # Vizinhos Santo Amaro das Brotas
  
  # Vizinhos Simão Dias
  
  # Vizinhos Siriri
  
  # Vizinhos São Cristóvao
  
  # Vizinhos São Domingos
  
  # Vizinhos São Francisco
  
  # Vizinhos São Miguel do Aleixo
  
  # Vizinhos Telha

  # Vizinhos Tobias Barreto
  
  edge_tobias_barreto_tomar_do_geru = Edge(vertex_tobias_barreto, vertex_tomar_do_geru, 47.9)
  
  graph_citys_sergipe.add_edge(edge_tobias_barreto_tomar_do_geru)
  
  # Vizinhos Umbauba