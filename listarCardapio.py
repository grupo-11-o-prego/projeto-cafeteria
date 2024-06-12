import cardapio as cp
def listar():    
   for cardapio_k, cardapio_v in cp.cardapio.items():
      for produtos_k, produtos_v in cardapio_v.items():
         for produto_k, produto_v in produtos_v.items():
            print("--------------------------------------------------")
            print(f"produto: {produto_k}")
            print(f"valor: R$ {produto_v['valor']:6.2f}")
            print(f"estoque: {produto_v['estoque']} unidades")
            print(f"categoria: {cardapio_k}")
            print(f"subcategoria: {produtos_k}")
         
listar()