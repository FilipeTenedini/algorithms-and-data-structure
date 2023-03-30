import { Pessoa } from "./Pessoa.js";

class Fisica extends Pessoa{
    constructor(id, mainName, fone, city, cpf){
        super(id, mainName, fone, city);
        this.cpf = cpf
    }
}

export { Fisica }