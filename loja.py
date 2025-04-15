from produto import Produto
from carrinho import Carrinho

class Loja:
    def __init__(self):
        self.produtos = []
        self.carrinho = Carrinho()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def listar_produtos(self):
        for i, produto in enumerate(self.produtos):
            print(f"{i + 1}. {produto}")
            
    def aplicar_desconto_promocional(self, indice, percetual):
        self.produtos[indice].aplicar_desconto(percetual)
        
    def adicionar_ao_carrinho(self, indice, quantidade):
        self.carrinho.adicionar(self.produtos[indice], quantidade)
        
    def simular_pagamento(self):
        total = self.carrinho.calcular_total()
        print(f"Total da compra: R${total:.2f}")
        print("Formas de pagamento:")
        print("1. dinheiro (5% de desconto)")
        print("2. PIX (10% de desconto)")
        print("3. Cartão de crédito á vista (sem desconto)")
        print("4. Cartão de crédito parcelado (5% de juros + divisão em parcelas)")
        
        opcao = input ("Escolha a forma de pagamento: ")
        if opcao == "1":
            total *= 0.95
        elif opcao == "2":
            total *= 0.90
        elif opcao == "3":
            total *= 1.00
        elif opcao == "4":
            total *= 1.05
            parcelas = int(input("Em quantas parcelas deseja pagar? "))
            valor_parcela = total / parcelas
            print(f"Pagamento em {parcelas}x de R${valor_parcela:.2f}")
            
        print(f"Valor final: R${total:.2f}")
        valor_pago = float(input('Digite o valor pago: R$'))
        
        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento aceito. Troco: R${troco:.2f}")
            self.carrinho.esvaziar()
        else:
            print("Pagamento insuficiente.")
        
    def estoque_total(self):
        for produto in self.produtos:
            print(f"{produto.nome}: {produto.estoque} unidades")