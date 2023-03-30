class Pedido{
    constructor(id, end, cliente){
        this.id = id;
        this.end = end;
        this.products = [];
        this.cliente = cliente
    }

    addProduto(prod){
        this.products.push(prod);
    }

    sumPrice(){
        let sum = 0;
        this.products.forEach(item => sum += item.price);
        return sum;
    }

    imprimir(){
        console.log(`
        id do pedido: ${this.id}
        Endereço do pedido: ${this.end}
        Nome do cliente: ${this.cliente.name}

        =====    Produtos    =====
        `)
        this.products.forEach(item => {
            console.log(`
        ${item.name} - ${item.cat.name} - R$ ${item.price.toFixed(2)}
            `)
        });
    }
}

export { Pedido }