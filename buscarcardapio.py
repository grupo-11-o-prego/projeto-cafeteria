import cardapio as cp
def buscar(cardapio):
    
    produto_desejado = input("Qual o produto desejado ?")
    for cardapio_k, cardapio_v in cp.cardapio.items():
         for produtos_k, produtos_v in cardapio_v.items():
            if produto_desejado in produtos_k:
               print(f"{produto_desejado} = {produtos_v} reais")


buscar(cp.cardapio)