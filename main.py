from model.entities import pessoa
from model.repositório import gerenciador_pessoas

gerenciador = gerenciador_pessoas.GerenciadorPessoas()

pessoa1 = pessoa.Pessoa(1, "Josue", "josue@gmail.com", 84927049, 22)
pessoa2 = pessoa.Pessoa(2, "Vinicius", "vinicius@gmail.com", 12345678, 22)

gerenciador.adicionar_pessoa(pessoa1)
gerenciador.adicionar_pessoa(pessoa2)

print("Lista de Pessoas:")
gerenciador.listar_pessoas()