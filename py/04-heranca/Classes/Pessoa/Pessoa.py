from Classes.Cidade.Cidade import Cidade

class Pessoa:

    def __init__(self, id=None, name=None, fone=None, city=Cidade(None, None)):
        self.id = id
        self.name = name
        self.fone = fone
        self.city = city

    def imprimir(self):
        print(self.id, self.name, self.fone, self.city.name)