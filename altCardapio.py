import cardapio as cp

categoria = cp.escolherCategoria()
subcategoria = cp.escolherSubCategoria(categoria)
produto = cp.escolherProduto(categoria, subcategoria)