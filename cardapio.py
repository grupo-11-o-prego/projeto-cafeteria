import json

arquivo = 'cardapio.txt'

# abre o arquivo e armazena os valores em uma variavel chamada 'cardapio_conteudo'
with open(arquivo, 'r') as arquivo_aberto:
  cardapio_conteudo = arquivo_aberto.read()
 
# transforma o conteudo do arquivo em um dicionário
cardapio = json.loads(cardapio_conteudo) 

carrinho = {"itens":[], "valor": 0}

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
    cardapio_json = json.dumps(cardapio)
    arquivo_aberto.write(str(cardapio_json))

def cadCardapio():
    validCat = False
    validSub = False
    print("========== CADASTRO DE PRODUTO NO CARDÁPIO ==========")
    categoria = escolherCategoria()
    subcategoria = escolherSubCategoria(categoria)
    nome = str(input("Informe o nome do produto a ser cadastrado: ")).lower()
    valor = float(input(f"Informe o valor do produto '{nome}': "))
    estoque = int(input(f"Informe a quantidade em estoque do produto '{nome}': "))
    cardapio[categoria][subcategoria][nome] = {'valor': valor, 'estoque': estoque}
    print(f"Adicionado: \n ===> {nome} <=== \n{cardapio[categoria][subcategoria][nome]}")
    salvar()
  
def altCardapio():
  categoria = escolherCategoria()
  subcategoria = escolherSubCategoria(categoria)
  produto = escolherProduto(categoria, subcategoria)

  while True:
    print("-- Opções ----------------------------------------")
    print(" [1] - Editar valor")
    print(" [2] - Editar estoque")
    print(" [3] - Sair")
    print("--------------------------------------------------")

    opcao = str(input("Escolha uma opção: "))
    if(opcao == "1"):
      valor = float(input(f"Entre com o novo valor de '{produto}': R$ "))
      cardapio[categoria][subcategoria][produto]["valor"] = valor
      print("Produto atualizado com sucesso!")
      salvar()
    elif(opcao == "2"):
      estoque = int(input(f"Entre com o novo estoque do '{produto}': "))
      cardapio[categoria][subcategoria][produto]["estoque"] = estoque
      print("Produto atualizado com sucesso!")
      salvar()
    elif(opcao == "3"):
      break
    else:
      print(f"> opção '{opcao}' não existe!")
    break

def remover_item(cardapio):

    print("\nSelecione para excluir o item desejado\n")
    categoria = escolherCategoria()
    subcategoria = escolherSubCategoria(categoria)
    produto = escolherProduto(categoria,subcategoria)
    
    cardapio[categoria][subcategoria].pop(produto)

    print(f"Produto {produto} excluído com sucesso!\n")

    salvar()

def buscar(cardapio):
    
   produto_desejado = input("Qual o produto desejado ? ")
   produto_achado = False
   for cardapio_k, cardapio_v in cardapio.items():
      for produtos_k, produtos_v in cardapio_v.items():
         for produto_k, produto_v in produtos_v.items():
            if produto_desejado in produto_k:
               print("--------------------------------------------------")
               print(f"produto: {produto_k}")
               print(f"valor: R$ {produto_v['valor']:6.2f}")
               print(f"estoque: {produto_v['estoque']} unidades")
               print(f"categoria: {cardapio_k}")
               print(f"subcategoria: {produtos_k}")
               produto_achado = True

   if(produto_achado == False):
      print(f"> o produto '{produto_desejado}' não existe!")
         
def listar():    
   for cardapio_k, cardapio_v in cardapio.items():
      for produtos_k, produtos_v in cardapio_v.items():
         for produto_k, produto_v in produtos_v.items():
            print("--------------------------------------------------")
            print(f"produto: {produto_k}")
            print(f"valor: R$ {produto_v['valor']:6.2f}")
            print(f"estoque: {produto_v['estoque']} unidades")
            print(f"categoria: {cardapio_k}")
            print(f"subcategoria: {produtos_k}")
