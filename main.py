from pessoa import Pessoa
from gerenciador_pessoas import GerenciadorPessoas


gerenciador = GerenciadorPessoas()

pessoa1 = Pessoa("Josue", "josue@gmail.com", 84927049, 22)
pessoa2 = Pessoa("Vinicius", "vinicius@gmail.com", 12345678, 22)

gerenciador.adicionar_pessoa(pessoa1)
gerenciador.adicionar_pessoa(pessoa2)

print("Lista de Pessoas:")
gerenciador.listar_pessoas()