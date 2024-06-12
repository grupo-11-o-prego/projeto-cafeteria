import cardapio as cp
import carrinho as cr

while True:
    print("\n\n")
    print("============= CAFETERIA 'O PREGO' ==============")
    print("--> AÇÕES:\n[1] - Administrar cardápio\n[2] - Realizar uma venda\n")
    acao = int(input("Escolha uma ação: "))
    while True:
        if (acao != 1) and (acao != 2):
            print("-----> Número inválido! Tente novamente.")
            break
        else:
            if acao == 1:
                print("\n\n")
                print("============= ADMINISTRAR CARDÁPIO ==============")
                print("--> AÇÕES:\n[1] - Cadastrar Produto\n[2] - Alterar produto\n[3] - Remover produto\n[4] - Buscar produto\n[5] - Listar todos os produtos\n[6] - Sair\n")
                acao2 = int(input("Escolha uma ação: "))
                if (acao2 != 1) and (acao2 != 2) and (acao2 != 3) and (acao2 != 4) and (acao2 != 5) and (acao2 != 6):
                    print("-----> Número inválido! Tente novamente.")
                else:
                    if acao2 == 1:
                        cp.cadCardapio()
                        break
                    elif acao2 == 2:
                        cp.altCardapio()
                        break
                    elif acao2 == 3:
                        cp.remover_item(cp.cardapio)
                        break
                    elif acao2 == 4:
                        cp.buscar(cp.cardapio)
                        break
                    elif acao2 == 5:
                        cp.listar()
                        break
                    elif acao2 == 6:
                        break
            elif acao == 2:
                print("\n\n")
                print("============= REALIZAR VENDA ==============")
                print("--> AÇÕES:\n[1] - Adicionar ao carrinho\n[2] - Remover do carrinho\n[3] - Visualizar carrinho\n[4] - Finalizar compra\n[5] - Sair\n")
                acao2 = int(input("Escolha uma ação: "))
                if (acao2 != 1) and (acao2 != 2) and (acao2 != 3) and (acao2 != 4) and (acao2 != 5):
                    print("-----> Número inválido! Tente novamente.")
                else:
                    if acao2 == 1:
                        cr.addCarrinho()
                        break
                    elif acao2 == 2:
                        cr.removeCarrinho()
                        break
                    elif acao2 == 3:
                        cr.mostrarCarrinho()
                        break
                    elif acao2 == 4:
                        cr.finalizarCompra()
                        break
                    elif acao2 == 5:
                        break
    