from Classes.Pessoa.Fisica import Fisica
from Classes.Cidade.Cidade import Cidade

pf = Fisica()
pf.nome = 'JOao'
pf.cidade = Cidade(3, 'Poa')
pf.imprimir()