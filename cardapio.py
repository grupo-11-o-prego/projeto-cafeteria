import json

arquivo = 'cardapio.txt'

# abre o arquivo e armazena os valores em uma variavel chamada 'cardapio_conteudo'
with open(arquivo, 'r') as arquivo_aberto:
  cardapio_conteudo = arquivo_aberto.read()
 
# transforma o conteudo do arquivo em um dicionário
cardapio = json.loads(cardapio_conteudo) 

def montarTitulo(texto: str = None):
  print("")

def exibirCategorias():
  print("-- Categorias ------------------------------------\n")
  for k in cardapio.keys():
    print(f" - {k}")
  print("--------------------------------------------------")

def exibirSubCategorias(categoria: str):
  print(f"-- Subcategorias de {categoria} {''.ljust(29 - len(categoria), '-')}")
  for k in cardapio[categoria].keys():
    print(f" - {k}")
  print("--------------------------------------------------")

def exibirProdutos(categoria: str, subcategoria: str):
  print("-- Produtos ------------------------------------\n")
  for k, produto in cardapio[categoria][subcategoria].items():
    print(f" - {k} - R${produto['valor']:6.2f} - {produto['estoque']} unidades")
  print("--------------------------------------------------")

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

def escolherCategoria():
  while True:
    exibirCategorias()
    categoria = str(input("Escolha uma categoria: ")).lower()
    if(verificarCategoria(categoria)):
      print("")
      return categoria
    else:
      print(f'> a categoria "{categoria}" não existe!')
    print("")
  
def escolherSubCategoria(categoria: str):
  while True:
    exibirSubCategorias(categoria)
    subcategoria = str(input("Escolha uma subcategoria: ")).lower()
    if(verificarSubCategoria(subcategoria, categoria)):
      print("")
      return subcategoria
    else:
      print(f'> a subcategoria "{subcategoria}" não existe!')
    print("")

def escolherProduto(categoria: str, subcategoria: str):
  while True:
    exibirProdutos(categoria, subcategoria)
    produto = str(input("Escolha um produto: ")).lower()
    if(verificarProduto(produto, subcategoria, categoria)):
      print("")
      return produto
    else:
      print(f'> o produto "{produto}" não existe!')
    print("")

def salvar(): 
  with open(arquivo, 'w') as arquivo_aberto:
    arquivo_aberto.write(str(cardapio))