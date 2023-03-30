import { Pessoa } from "./Pessoa.js";

class Juridica extends Pessoa{
    constructor(id, mainName, fone, city, cnpj){
        super(id, mainName, fone, city);
        this.cpf = cnpj;
    }
}

export { Juridica }