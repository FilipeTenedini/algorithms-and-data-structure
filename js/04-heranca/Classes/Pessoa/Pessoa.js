class Pessoa{
    constructor(id, mainName, fone, city){
        this.id = id
        this.mainName = mainName;
        this.fone = fone;
        this.city = city
    }

    imprimir(){
        console.log(this.id, this.name, this.fone, this.city);
    }
}        

export { Pessoa }