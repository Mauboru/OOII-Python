from Conexao import Conexao
from GerenciadorPessoas import GerenciadorPessoas
from PessoaDAO import PessoaDAO

pessoaDAO = PessoaDAO(Conexao.conectar_banco_dados())

gerenciador = GerenciadorPessoas(pessoaDAO)

#nome = "Josue"
#email = "josue@gmail.com" 
#telefone = 80028922
#idade = 22

#gerenciador.adicionar_pessoa(nome, email, telefone, idade)

print("Lista de Pessoas:")
lista_pessoas = gerenciador.listar_pessoas()

for pessoa in lista_pessoas:
    print(pessoa)


