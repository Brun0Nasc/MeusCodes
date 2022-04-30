from cliente import Cliente
from mercadoria import Mercadoria
from cadastro import Cadastro

cadastroCliente = Cadastro()
cadastroMercadoria = Cadastro()
outroCadastro = cadastroCliente

cliente1 = Cliente()
cliente2 = Cliente('Joana', 22, 1500)
cliente3 = Cliente(nome = "João", idade = 19)

cadastroCliente.adiciona(cliente1)
cadastroCliente.adiciona(cliente2)
cadastroCliente.adiciona(cliente3)

mercadoria1 = Mercadoria('Computador', 2500)
mercadoria2 = Mercadoria('Ventilador', 150)

cadastroMercadoria.adiciona(mercadoria1)
cadastroMercadoria.adiciona(mercadoria2)

cliente4 = Cliente("Bruno", 21, 3000)
outroCadastro.adiciona(cliente4)

cadastroCliente.imprimeTodos()
print()
outroCadastro.imprimeTodos()
