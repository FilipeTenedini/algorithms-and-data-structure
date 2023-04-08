from Classes.Pessoa.Pessoa import Pessoa
from Classes.Pessoa.Fisica import Fisica
from Classes.Cidade.Cidade import Cidade

class Juridica(Pessoa):

    def __init__(self, name, fone, cnpj, city=Cidade(None, None)):
        super().__init__(None, name, fone, city)
        self.cnpj = cnpj
        self.employee_qt = 0
        self.employees = []
    
    def addEmployee(self, funcionario):
        self.employees.append(funcionario)
        self.employee_qt += 1

    def printStatus(self):
        print('\n')
        print(f'Empresa: {self.name}')
        print(f'Fone: {self.fone}')
        print(f'Cidade {self.city.name}')
        print(f'Qtd Funcionários: {self.employee_qt}')
        if len(self.employees) > 0:
            print('\nFuncionários:')
            for employee in self.employees:
                print(f'Nome funcionário: {employee.name}')
                print(f'Fone funcionário: {employee.fone}')
                print(f'Nome funcionário: {employee.city.name}')
                print(" --------------------------------- ")
