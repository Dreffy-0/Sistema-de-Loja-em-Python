class Carrinho:
    def __init__(self):
        self.itens = {}
        
    def adicionar(self, produto, quantidade):
        if produto.estoque >= quantidade:
            if produto.nome in self.itens:
                self.itens[produto.nome]["quantidade"] += quantidade
            else:
                self.itens[produto.nome] = {
                    "produto": produto,
                    "quantidade": quantidade
                }
            produto.estoque -= quantidade
        else:
            print("Estoque insuficiente")
    
    def calcular_total(self):
        return sum(item["produto"].preco_final() * item["quantidade"] for item in self.itens.values())
    
    def visualizar(self):
        for item in self.itens.values():
            p = item["produto"]
            q = item["quantidade"]
            v = p.preco_final()
            print(f"{p.nome} - R${v:.2f} x {q}")
    
    def esvaziar(self):
        self.itens.clear()
    
    def vazio(self):
        return len(self.itens) == 0