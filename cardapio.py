import json

arquivo = 'cardapio.txt'

# abre o arquivo e armazena os valores em uma variavel chamada 'cardapio_conteudo'
with open(arquivo, 'r') as arquivo_aberto:
  cardapio_conteudo = arquivo_aberto.read()
 
# transforma o conteudo do arquivo em um dicionário
cardapio = json.loads(cardapio_conteudo) 

def exibirCategorias():
  for k in cardapio.keys():
    print(f"{k}")

def verificarCategoria(categoria: str):
  return categoria.lower() in cardapio.keys()

def salvar(): 
  with open(arquivo, 'w') as arquivo_aberto:
    arquivo_aberto.write(str(cardapio))