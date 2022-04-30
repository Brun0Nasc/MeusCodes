class Cliente:
    def __init__(self, nome="Fulano", idade=18, saldo=0):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
    
    def imprimeFicha(self):
        print("Nome: ", self.nome)
        print("Idade", self.idade)
        print("Saldo", self.saldo)
    
    def aumentaSalario(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return self.nome+";"+str(self.idade)+";"+str(self.saldo)
