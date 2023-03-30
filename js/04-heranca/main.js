import { Cidade } from "./Classes/Cidade/Cidade.js"
import { Pessoa } from "./Classes/Pessoa/Pessoa.js";
import { Fisica } from "./Classes/Pessoa/Fisica.js";

const c1 = new Cidade(0, 'Porto Alegre')
const p1 = new Fisica(1, 'Filipe', '3368053029', c1, '746-932-320-12')

console.log(p1)