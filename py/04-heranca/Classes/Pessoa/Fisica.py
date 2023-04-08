from Classes.Pessoa.Pessoa import Pessoa
from Classes.Cidade.Cidade import Cidade

class Fisica(Pessoa):

    def __init__(self, name, fone, city, cpf):
        super().__init__(id, name, fone, city)
        self.cpf = cpf
        self.company = None

    def setCompany(self, company):
        self.company = company