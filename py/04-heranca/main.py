from Classes.Pessoa.Fisica import Fisica
from Classes.Cidade.Cidade import Cidade

pf = Fisica()
pf.nome = 'Joao'
pf.cidade = Cidade(3, 'Poa')
pf.id = 2
pf.fone = '336805329'
pf.imprimir()