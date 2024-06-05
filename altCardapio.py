import cardapio as cp

categoria = cp.escolherCategoria()
subcategoria = cp.escolherSubCategoria(categoria)
produto = cp.escolherProduto(categoria, subcategoria)

print("-- Opções ----------------------------------------")
print(" [1] - Editar valor")
print(" [2] - Editar estoque")
print("--------------------------------------------------")

