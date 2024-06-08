import cardapio as cp

def mostrarCarrinho():
    print("============ Carrinho ============")
    for x in cp.carrinho['itens']:
        print(f'---> {x["nome"]} - R${x["valor"]} - Qtd: {x["quantidade"]}')
    print(f"---------------> Valor TOTAL: R${cp.carrinho['valor']}")

def addCarrinho():
    novamente = True
    while novamente == True:
        categoria = cp.escolherCategoria()
        subcategoria = cp.escolherSubCategoria(categoria)
        cont = 1
        inputItem = []
        print("=========== Produtos: ===========")
        for x in cp.cardapio[categoria][subcategoria]:
            inputItem.append(x)
            print(f"[{cont}] - {x} R${cp.cardapio[categoria][subcategoria][x]['valor']} (Estoque: {cp.cardapio[categoria][subcategoria][x]['estoque']})")
            cont += 1
        valido = False
        while valido == False:
            numeroInput = int(input("-----> Escolha o número do produto: "))
            if (numeroInput < 1) or (numeroInput > len(inputItem)):
                print("---> Número inválido! Tente novamente.")
            else:
                valido = True
        itemSelecionado = inputItem[numeroInput - 1]
        print("Item selecionado:", itemSelecionado)
        valido = False
        while valido == False:
            quantidadeItem = int(input("Informe a quantidade a ser colocada no carrinho: "))
            if quantidadeItem < 1:
                print("---> É necessário adicionar pelo menos 1 item ao carrinho.")
            elif quantidadeItem > cp.cardapio[categoria][subcategoria][itemSelecionado]['estoque']:
                print(f"---> O número excede a quantidade do item '{itemSelecionado}' no estoque (Quantidade: {cp.cardapio[categoria][subcategoria][itemSelecionado]['estoque']})")
            else:
                valido = True
            precoItem = cp.cardapio[categoria][subcategoria][itemSelecionado]['valor']
            cp.carrinho['itens'].append({'nome': itemSelecionado, 'valor': precoItem ,'quantidade': quantidadeItem})
            cp.carrinho['valor'] += precoItem * quantidadeItem

        continuar = str(input("Quer adicionar mais um item ao carrinho? [s/n]")).lower()
        if continuar == 'n':
            novamente = False
    
def removeCarrinho():
    print("=============== REMOVER ITEM ===============")
    cont = 1
    inputItem = []
    print("=========== Produtos: ===========")
    for x in cp.carrinho['itens']:
        inputItem.append(x)
        print(f'---> [{cont}] {x["nome"]} - R${x["valor"]} - Qtd: {x["quantidade"]}')
        cont += 1
    valido = False
    while valido == False:
        numeroInput = int(input("-----> Escolha o número do produto a ser removido: "))
        if (numeroInput < 1) or (numeroInput > len(cp.carrinho['itens'])):
            print("---> Número inválido! Tente novamente.")
        else:
            valido = True
    itemSelecionado = inputItem[numeroInput - 1]
    cp.carrinho['itens'].pop(itemSelecionado)

addCarrinho()
removeCarrinho()
mostrarCarrinho()
