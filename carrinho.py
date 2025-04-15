class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionarProduto(self, produto, quantidade):
        if produto.estoque >= quantidade:
            self.itens.append((produto, quantidade))
            produto.estoque -= quantidade
        else:
            print("Estoque vazio!")

    def exibirItensCarrinho(self):
        i = 0
        while i < len(self.itens):
            produto, quantidade = self.itens[i]
            print(f"{i + 1}. {produto} - Quantidade: {quantidade}")
            i += 1

    def calcularTotal(self):
        return sum(produto.preco * quantidade for produto, quantidade in self.itens)

    def esvaziarCarrinho(self):
        self.itens.clear()
        print("Carrinho esvaziado!")
