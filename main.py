from loja import Loja
from produto import Produto

def menu():
    loja = Loja()
    loja.adicionar_produto(Produto("Notebook Asus Vivobook 15", 2560, 5))
    loja.adicionar_produto(Produto("Notebook Asus Vivobook 16", 3200, 3))
    loja.adicionar_produto(Produto("Notebook Asus Vivobook 16", 3300, 4))
    loja.adicionar_produto(Produto("Notebook Acer Aspire 5", 3300, 4))
    loja.adicionar_produto(Produto("Smartphone Samsung Galaxy S23 Ultra", 4000, 6))
    loja.adicionar_produto(Produto("Smartphone Samsung Galaxy S24", 3500, 8))
    loja.adicionar_produto(Produto("Smartphone Samsung Galaxy S24 Fe", 3254, 10))
    loja.adicionar_produto(Produto("Smartphone iPhone 16", 5357, 7))
    loja.adicionar_produto(Produto("Smartphone iPhone 15", 5100, 10))
    loja.adicionar_produto(Produto("Smartphone iPhone 16 Pro Max", 9900, 2))
    
    while True:
        print("\n--- Menu da Loja ---")
        print("1. Listar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Visualizar carrinho")
        print("4. Aplicar desconto")
        print("5. Finalizar compra")
        print("6. Ver estoque")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            loja.listar_produtos()
        elif opcao == "2":
            loja.listar_produtos()
            i = int(input("Número do produto: ")) - 1
            q = int(input("Quantidade: "))
            loja.adicionar_ao_carrinho(i, q)
        elif opcao == "3":
            loja.carrinho.visualizar()
        elif opcao == "4":
            loja.listar_produtos()
            i = int(input("Produto para desconto: ")) - 1
            d = float(input("Percentual de desconto: "))
            loja.aplicar_desconto_promocional(i, d)
        elif opcao == "5":
            if loja.carrinho.vazio():
                print("Carrinho vazio.")
            else:
                loja.simular_pagamento()
        elif opcao == "6":
            loja.estoque_total()
        elif opcao == "7":
            break
        else: print("Opção inválida. Tente novamente.")        

if __name__ == "__main__":
    menu()
    