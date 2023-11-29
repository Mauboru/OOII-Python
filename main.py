from Conexao import Conexao
from GerenciadorPessoas import GerenciadorPessoas
from PessoaDAO import PessoaDAO

pessoaDAO = PessoaDAO(Conexao.conectar_banco_dados())

gerenciador = GerenciadorPessoas(pessoaDAO)

