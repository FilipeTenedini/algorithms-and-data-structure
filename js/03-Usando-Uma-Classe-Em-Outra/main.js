import { Pessoa } from "./Pessoa.js";
import { Cidade } from "./Cidade.js";
import { Pedido } from "./Pedido.js";
import { Categoria } from "./Categoria.js";
import { Produto } from "./Produto.js";

const cit1 = new Cidade(1, 'Porto Alegre');
const pers1 = new Pessoa('filipe', 13, cit1);
const cat1 = new Categoria(1, 'bebida');
const cat2 = new Categoria(2, 'alimento');
const prod1 = new Produto(1, 'Coca-Cola', 3.80, cat1);
const prod2 = new Produto(2, 'arroz', 5.50, cat2);
const ped1 = new Pedido(0, 'Hugo Nelson, 25', pers1);

ped1.addProduto(prod1)
ped1.addProduto(prod2)

ped1.imprimir()
console.log(`Total ${ped1.sumPrice()}`)