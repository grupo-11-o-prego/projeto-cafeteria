import cardapio as cp

categoria = cp.escolherCategoria()
subcategoria = cp.escolherSubCategoria(categoria)
produto = cp.escolherProduto(categoria, subcategoria)

while True:
  print("-- Opções ----------------------------------------")
  print(" [1] - Editar valor")
  print(" [2] - Editar estoque")
  print("--------------------------------------------------")

  opcao = str(input("Escolha uma opção: "))
  if(opcao == "1"):
    valor = float(input(f"Entre com o novo valor de '{produto}': R$ "))
    cp.cardapio[categoria][subcategoria][produto]["valor"] = valor
    print("Produto atualizado com sucesso!")
    cp.salvar()
  elif(opcao == "2"):
    estoque = int(input(f"Entre com o novo estoque do '{produto}': "))
    cp.cardapio[categoria][subcategoria][produto]["estoque"] = valor
    print("Produto atualizado com sucesso!")
    cp.salvar()
  else:
    print(f"> opção '{opcao}' não existe!")


