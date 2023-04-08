import { Cidade } from "./Classes/Cidade/Cidade.js";
import { Fisica } from "./Classes/Pessoa/Fisica.js";
import { Juridica } from "./Classes/Pessoa/Juridica.js";

const c1 = new Cidade(1, 'Porto Alegre');
const c2 = new Cidade(2, 'Capão da Canoa');

const joao = new Fisica(1, 'João', '3368-5321', c1, '012-432-120-32');
const maria = new Fisica(2, 'Maria', '5321-3368', c2, '432-120-012-32');
const jose = new Fisica(3, 'Jose', '5321-3368', c2, '142-302-130-22');

const dosul = new Juridica(1, 'Supermercado Dosul', '9864-9012', c2, '03-123-245/0001-00');


dosul.addEmployee(maria);
dosul.addEmployee(jose);

dosul.logStatus();