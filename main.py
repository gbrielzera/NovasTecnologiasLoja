from carrinho import Carrinho
from loja import Loja

def menu():
    loja = Loja()
    carrinho = Carrinho()

    while True:
        print("\nBem vindo a loja de roupas Gabriel UCB!")
        print("1. Ver produtos")
        print("2. Adicionar ao carrinho")
        print("3. Ver carrinho")
        print("4. Remover um produto do carrinho")
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
            carrinho.exibirItensCarrinho()
            print(f"Total: R${carrinho.calcularTotal():.2f}")

        elif opcao == "4":
            if not carrinho.itens:
                print("Carrinho vazio!")
                continue
                
            carrinho.exibirItensCarrinho()
            try:
                indice = int(input("Digite o número do item para remover: ")) - 1
                carrinho.removerProduto(indice)
            except ValueError:
                print("Entrada inválida!")

        elif opcao == '5':
            loja.realizar_pagamento(carrinho)

        elif opcao == '6':
            print("\n")
            print("Saindo da loja Gabriel UCB, volte sempre!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__": 
    menu()
