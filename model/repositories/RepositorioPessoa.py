from model.entities.Pessoa import Pessoa
from model.daos.PessoaDAO import PessoaDAO
from model.daos.Conexao import Conexao
from colorama import Fore

class RepositorioPessoa:
    def __init__(self, pessoaDAO):
        self.pessoaDAO = pessoaDAO

    def adicionar_pessoa(self, nome, email, telefone, idade):
        nova_pessoa = Pessoa(nome, email, telefone, idade)
        return self.pessoaDAO.criar(nova_pessoa)

    def listar_pessoas(self):
        return self.pessoaDAO.listar()

    def buscar_pessoa(self, id):
        return self.pessoaDAO.buscarPorId(id)

    def atualizar_pessoa(self, id, novo_nome, novo_email, novo_telefone, novo_idade):
        pessoa_atualizada = Pessoa(id, novo_nome, novo_email, novo_telefone, novo_idade)
        return self.pessoaDAO.atualizar(pessoa_atualizada)

    def excluir_pessoa(self, id):
        return self.pessoaDAO.deletar_pessoa(id)