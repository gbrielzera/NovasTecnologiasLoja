from carrinho import Carrinho
from loja import Loja

def menu():
    loja = Loja()
    carrinho = Carrinho()

    while True:
        print("\nBem vindo a loja de roupas UCB!")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Aplicar desconto")
        print("4. Ver carrinho")
        print("5. Finalizar compra")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n")
            loja.exibirProdutos()

        elif opcao == '2':
            print("\n")
            loja.exibirProdutos()
            try:
                print("\n")
                i = int(input("Escolha o produto: "))
                i -= 1
                q = int(input("Escolha a quantidade: "))
                produto = loja.getProduto(i)
                if produto:
                    carrinho.adicionarProduto(produto, q)
                    print(f"Produto {produto.nome} adicionado ao carrinho.")
            
            except:
                print("Entrada inválida.")

        elif opcao == '3':
            print("\n")
            loja.exibirProdutos()
            try:
                i = int(input("Escolha o numero do produto para aplicar o desconto: "))
                i -= 1
                p = float(input("Escolha o percentual desconto sem o % (Ex: 10, 3.5, 45): "))
                produto = loja.getProduto(i)
                if produto:
                    produto.usarDesconto(p)
                    print(f"Desconto de {p}% aplicado ao produto {produto.nome}.")
            except:
                print("Entrada inválida.")

        elif opcao == '4':
            print("\n")
            carrinho.exibirItensCarrinho()
            print(f"Total: R${carrinho.calcularTotal():.2f}")

        elif opcao == '5':
            print("\n")
            total = carrinho.calcularTotal()
            print(f"Total da compra: R${total:.2f}")
            valor = float(input("Digite o valor a ser pago: "))
            if valor >= total:
                print(f"Compra finalizada! Troco: R${valor - total:.2f}")
                carrinho.esvaziarCarrinho()
            else:
                print("Valor insuficiente!")
        
        elif opcao == '6':
            print("\n")
            print("Saindo da loja UCB, volte sempre!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__": 
    menu()

