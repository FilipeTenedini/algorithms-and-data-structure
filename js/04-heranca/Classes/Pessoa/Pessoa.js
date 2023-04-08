class Pessoa{
    constructor(id, mainName, fone, city){
        this.id = id;
        this.mainName = mainName;
        this.fone = fone;
        this.city = city;
    }

    imprimir(){
        console.log(`${this.id}, ${this.mainName}, ${this.fone}, ${this.city.name}`);
    }
}        

export { Pessoa }