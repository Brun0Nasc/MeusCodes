class Mercadoria:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return self.nome+";"+str(self.preco)