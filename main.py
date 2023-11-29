from model.daos.Conexao import Conexao
from model.repositories.RepositorioPessoa import RepositorioPessoa
from model.daos.PessoaDAO import PessoaDAO

pessoaDAO = PessoaDAO(Conexao.conectar_banco_dados())
gerenciador = RepositorioPessoa(pessoaDAO)

nova_pessoa = gerenciador.adicionar_pessoa("teste", "jean@email.com", "55449988", 28)
print(nova_pessoa)