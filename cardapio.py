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

def exibirSubCategorias(categoria: str):
  for k in cardapio[categoria].keys():
    print(f"{k}")

def verificarCategoria(categoria: str):
  return categoria.lower() in cardapio.keys()

def verificarSubCategoria(subcategoria: str, categoria: str):
  categoria_lowercase = categoria.lower()

  if verificarCategoria(categoria_lowercase) == False:
    return False

  return subcategoria.lower() in cardapio[categoria_lowercase].keys()

def verificarProduto(produto: str, subcategoria: str, categoria: str):
  categoria_lowercase = categoria.lower()

  if verificarCategoria(categoria_lowercase) == False:
    return False
  
  subcategoria_lowercase = subcategoria.lower()

  if verificarSubCategoria(subcategoria_lowercase, categoria_lowercase) == False:
    return False

  return produto.lower() in cardapio[categoria_lowercase][subcategoria_lowercase].keys()

def salvar(): 
  with open(arquivo, 'w') as arquivo_aberto:
    arquivo_aberto.write(str(cardapio))