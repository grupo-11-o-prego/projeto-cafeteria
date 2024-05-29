import cardapio as cp

def remover_item(cardapio):
    cp.exibirCategorias()
    categoria = str(input("O item que deseja excluir faz parte de qual categoria?\n"))
    categoria.lower()

    validacaoCategoria = False

    while validacaoCategoria == False:
        print("CATEGORIA INVÁLIDA!\nPor favor digite novamente\n")
        cp.exibirCategorias()
        categoria = str(input("\nO item que deseja excluir faz parte de qual categoria?\n"))
        categoria.lower()

        if cp.verificarCategoria(categoria) == True:
            validacaoCategoria = True
        else:
            validacaoCategoria = False
    
    if categoria == "bebidas":
        cp.exibirSubCategorias()
        subcategoria = str(input("O item que deseja excluir faz parte de qual subcategoria?"))
        subcategoria.lower()

        validacaoSubcategoria = False

        while validacaoSubcategoria == False:
            print("SUBCATEGORIA INVÁLIDA!\nPor favor digite novamente\n")
            cp.exibirSubCategorias()
            subcategoria = str(input("\nO item que deseja excluir faz parte de qual subcategoria?\n"))
            subcategoria.lower()

            if cp.verificarCategoria(subcategoria) == True:
                validacaoSubcategoria = True
            else:
                validacaoSubcategoria = False
        
        if subcategoria == "refrigerantes":
            cp.exibirItens()
            item = str(input("Qual item você deseja excluir?"))
            item.lower()

            validacaoItem = False

            while validacaoItem == False:
                print("SUBCATEGORIA INVÁLIDA!\nPor favor digite novamente\n")
                cp.exibirSubCategorias()
                item = str(input("\nQual item você deseja excluir?\n"))
                item.lower()

                if cp.verificarCategoria(item) == True:
                    validacaoItem = True
                else:
                    validacaoItem = False
            
            if item == "coca-cola":
                excluido = cardapio.pop("coca-cola")
                print(f"Item {excluido} removido com sucesso!")



remover_item()