from produto import Produto

class Loja:
    def __init__(self):
        self.produtos = [
            Produto("Camisa branca", 49.99, 10),
            Produto("Calça Jeans", 89.99, 15),
            Produto("Tênis esportivo", 249.99, 20),
            Produto("Boné preto", 79.99, 5),
            Produto("Cinto de couro", 129.99, 5),
            Produto("Moletom", 99.99, 10),
            Produto("Sapato social", 199.99, 8),
            ]
    


    def exibirProdutos(self):
        i = 0
        while i < len(self.produtos):
            produto = self.produtos[i]
            print(f"{i + 1}. {produto}")
            i += 1

    def getProduto(self, indice):
        if 0 <= indice < len(self.produtos):
            return self.produtos[indice]
        else:
            print("Produto não encontrado!")
            return None