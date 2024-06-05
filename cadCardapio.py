import cardapio as cp

def cadCardapio():
    validCat = False
    validSub = False
    print("========== CADASTRO DE PRODUTO NO CARDÁPIO ==========")
    categoria = cp.escolherCategoria()
    subcategoria = cp.escolherSubCategoria(categoria)
    nome = str(input("Informe o nome do produto a ser cadastrado: ")).lower()
    valor = float(input(f"Informe o valor do produto '{nome}': "))
    estoque = int(input(f"Informe a quantidade em estoque do produto '{nome}': "))
    cp.cardapio[categoria][subcategoria][nome] = {'valor': valor, 'estoque': estoque}
    print(f"Adicionado: \n ===> {nome} <=== \n{cp.cardapio[categoria][subcategoria][nome]}")
    cp.salvar()
cadCardapio()
