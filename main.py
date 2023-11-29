from Conexao import Conexao
from GerenciadorPessoas import GerenciadorPessoas
from PessoaDAO import PessoaDAO

pessoaDAO = PessoaDAO(Conexao.conectar_banco_dados())
gerenciador = GerenciadorPessoas(pessoaDAO)

nova_pessoa = gerenciador.adicionar_pessoa("Vinicius Henrique", "vinicius@email.com", "84687559", 28)