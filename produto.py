class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.desconto = 0

    def aplicar_desconto(self, percentual):
        self.desconto = percentual
    
    def preco_final(self):
        return self.preco * (1 - self.desconto / 100)

    def __str__(self):
        valor = self.preco_final()
        return f"{self.nome} - R$ {valor:.2f} - Estoque: {self.estoque}"