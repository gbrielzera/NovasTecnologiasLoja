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
        
    def realizar_pagamento(self, carrinho):
        if not carrinho.itens:
            print("Carrinho vazio.")
            return

        print("\nFormas de pagamento:")
        print("1 - Débito (5% de desconto)")
        print("2 - Crédito (10% de taxa)")
        print("3 - Pix (15% de desconto)")

        opcao = input("Escolha a forma de pagamento (1, 2 ou 3): ")
        total = carrinho.calcularTotal()

        if opcao == "1":
            desconto = total * 0.05
            total -= desconto
            print(f"\nDesconto de R$ {desconto:.2f} aplicado.")
        elif opcao == "2":
            taxa = total * 0.10
            total += taxa
            print(f"\nTaxa de R$ {taxa:.2f} adicionada.")
        elif opcao == "3":
            desconto = total * 0.15
            total -= desconto
            print(f"\nDesconto de R$ {desconto:.2f} aplicado.")
        else:
            print("\nForma de pagamento inválida.")
            return

        print(f"Total a pagar: R$ {total:.2f}")

        while True:
            try:
                valor_pago = float(input("\nDigite o valor pago: R$ "))
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            if valor_pago >= total:
                troco = valor_pago - total
                print(f"\nPagamento concluído com troco de R$ {troco:.2f}")
                carrinho.esvaziarCarrinho()
                break
            else:
                print(f"Pagamento insuficiente. Você precisa pagar pelo menos R$ {total:.2f}.")

