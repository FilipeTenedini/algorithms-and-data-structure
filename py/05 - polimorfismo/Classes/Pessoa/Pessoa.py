from Classes.Cidade.Cidade import Cidade

class Pessoa:

    def __init__(self, id=None, name=None, fone=None, city=Cidade(None, None)):
        self.id = id
        self.name = name
        self.fone = fone
        self.city = city

    def __str__(self):
        return f"Nome: {self.name}\nFone: {self.fone}\nCidade: {self.city.name}"
    
    def imprimir(self):
        print(f'{self.id}\n{self.name}\n{self.fone}\n{self.city.name}')
        