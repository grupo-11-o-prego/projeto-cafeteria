import json
arquivo = 'cardapio.txt'

# abre o arquivo e armazena os valores em uma variavel chamada 'cardapio_conteudo'
with open(arquivo, 'r') as file:
  cardapio_conteudo = file.read()
 
# transforma o conteudo do arquivo em um dicionário
cardapio = json.loads(cardapio_conteudo)    