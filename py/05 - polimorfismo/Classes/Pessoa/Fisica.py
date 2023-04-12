from Classes.Pessoa.Pessoa import Pessoa
from Classes.Cidade.Cidade import Cidade

class Fisica(Pessoa):

    def __init__(self, name, fone, city, cpf):
        super().__init__(id, name, fone, city)
        self.cpf = cpf
        self.company = None

    def __str__(self):
        return super().__str__() + f"\nCPF: {self.cpf}"

    def setCompany(self, company):
        self.company = company

    def imprimir(self):
        super().imprimir()
        print(self.cpf)