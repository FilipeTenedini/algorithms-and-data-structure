import { Pessoa } from "./Pessoa.js";

class Juridica extends Pessoa{
    constructor(id, mainName, fone, city, cnpj){
        super(id, mainName, fone, city);
        this.cnpj = cnpj;
        this.employees_qt = 0;
        this.employees = [];
    }

    addEmployee(employee){
        this.employees.push(employee);
        this.employees_qt ++;
    }

    logStatus(){
        console.log(`Empresa: ${this.mainName}`);
        console.log(`Fone: ${this.fone}`);
        console.log(`Cidade ${this.city.name}`);
        console.log(`Qtd Funcionários: ${this.employees_qt}`);

        if (this.employees.length > 0) {
            console.log('\nFuncionários:');

            for (const emp of this.employees){
                console.log(`Nome funcionário: ${emp.mainName}`);
                console.log(`Fone funcionário: ${emp.fone}`);
                console.log(`Nome funcionário: ${emp.city.name}`);
                console.log('--------------------------------- ');
            }
        }
    }

}

export { Juridica }