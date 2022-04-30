class Cadastro:
    def __init__(self):
        self.lista = []
    
    def adiciona(self, objeto):
        self.lista.append(objeto)
    
    def imprimeTodos(self):
        for e in self.lista:
            print(e)