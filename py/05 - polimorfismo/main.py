from Classes.Pessoa.Pessoa import Pessoa
from Classes.Pessoa.Fisica import Fisica
from Classes.Pessoa.Juridica import Juridica
from Classes.Cidade.Cidade import Cidade

c1 = Cidade(1, 'PoA')
p1 = Pessoa(1, 'Faiska', '3237-2920', c1)
p2 = Fisica('Filipe', '3237-2020', c1, '033123091-32')

print(p2)