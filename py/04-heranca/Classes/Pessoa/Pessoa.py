from Classes.Cidade.Cidade import Cidade

class Pessoa:

    def __init__(self, id = None, nome = None, fone = None, cidade = Cidade(None, None)):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.cidade = cidade

    def imprimir(self):
        print(self.id, self.nome, self.fone, self.cidade.nome)