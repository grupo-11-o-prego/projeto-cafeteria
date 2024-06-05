import cardapio as cp

def remover_item(cardapio):

    print("\nSelecione para excluir o item desejado\n")
    categoria = cp.escolherCategoria()
    subcategoria = cp.escolherSubCategoria(categoria)
    produto = cp.escolherProduto(categoria,subcategoria)
    
    cardapio[categoria][subcategoria].pop(produto)

    print(f"Produto {produto} excluído com sucesso!\n")

    cp.salvar()

remover_item(cp.cardapio)