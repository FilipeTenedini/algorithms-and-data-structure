class Produto:

    def __init__(self,id, nome, preco, cat):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.cat = cat
    
    
    def imprimir(self):
        print(f"id pedido: {self.id}")
        print(f"endereço: {self.nome}")
        print(f"preco: {self.preco}")
        print(f"categoria: {self.cat}")