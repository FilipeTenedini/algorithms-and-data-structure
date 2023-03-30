from Categoria import Categoria
from Produto import Produto
from Pedido import Pedido

cat1 = Categoria(1, 'bebidas')
cat2 = Categoria(2, 'alimentos')

meuPedido = Pedido(1, 'hugo nelson, 25', 'Rafael')

meuPedido.addProduto(Produto(1, 'coca-cola', 4.90, cat1))
meuPedido.addProduto(Produto(2, 'guarana', 4.90, cat1))
meuPedido.addProduto(Produto(3, 'batata', 0.90, cat2))
preco = meuPedido.sumPrice()
meuPedido.imprimir()
print("Preço total do pedido: R$%.2f" % preco)
