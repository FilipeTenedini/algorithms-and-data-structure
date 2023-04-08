from Classes.Pessoa.Pessoa import Pessoa
from Classes.Pessoa.Fisica import Fisica
from Classes.Pessoa.Juridica import Juridica
from Classes.Cidade.Cidade import Cidade

c1 = Cidade(1, 'Porto Alegre')
c2 = Cidade(2, 'Capão da Canoa')

joao = Fisica('João', '3368-5321', c1, '012-432-120-32')
maria = Fisica('Maria', '5321-3368', c2, '432-120-012-32')
jose = Fisica('Jose', '5321-3368', c2, '142-302-130-22')

dosul = Juridica('Supermercado Dosul', '9864-9012', '03-123-245/0001-00', c2)


dosul.printStatus()


dosul.addEmployee(joao)
dosul.addEmployee(jose)
dosul.printStatus()
