class Pedido:

    def __init__(self, id, end, cliente):
        self.id = id
        self.end = end
        self.cliente = cliente
        self.produtos = []
        
    def addProduto(self, item):
        self.produtos.append(item)
    
    def sumPrice(self):
        if len(self.produtos) == 0:
            print('Pedido vazio.')
        else:
            soma = 0
            for produto in self.produtos:
                soma += produto.preco
            return soma
      
    def imprimir(self):
        print(f"id pedido: {self.id}")
        print(f"cliente: {self.cliente}")
        print(f"endereço: {self.end}")
        print("\n\n==== itens ====")
        for produto in self.produtos:
            print(produto.nome)
            print(f"{produto.preco} - {produto.cat.nome}")
