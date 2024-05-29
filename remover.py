def remover_item():
    categoria = str(input("Bebida\nEntradas\nPratos Principais\nSobremesas\nO item que deseja excluir faz parte de qual categoria?\n"))
    categoria.lower()

    validacao = False

    while validacao == False:
        print("CATEGORIA INVÁLIDA!\nPor favor digite novamente\n")
        categoria = str(input("Bebida\nEntradas\nPratos Principais\nSobremesas\nO item que deseja excluir faz parte de qual categoria?\n"))
        categoria.lower()

        if categoria == "bebida" or categoria == "entradas" or categoria == "pratos principais" or categoria == "Sobremesas":
            validacao = True
        else:
            validacao = False
    
    if categoria == "bebida":
        refri,suco,cafe,cha,

    elif categoria == "entrada":
        a

    elif categoria == "pratos principais":
        a

    elif categoria == "sobremesas":
        a


remover_item()