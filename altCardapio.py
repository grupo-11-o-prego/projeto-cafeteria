import cardapio as cp

categoria = cp.escolherCategoria()
subcategoria = cp.escolherSubCategoria(categoria)

cp.exibirProdutos(categoria, subcategoria)
produto = input("produto: ")
cp.cardapio.pop(produto)
print(cp.cardapio)