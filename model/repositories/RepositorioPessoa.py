from model.entities.Pessoa import Pessoa
from model.daos.PessoaDAO import PessoaDAO
from model.daos.Conexao import Conexao

class RepositorioPessoa:
    def __init__(self, pessoaDAO):
        self.pessoaDAO = pessoaDAO

    def adicionar_pessoa(self, nome, email, telefone, idade):
        novaPessoa = Pessoa(nome, email, telefone, idade)
        return self.pessoaDAO.criar(novaPessoa)

    def listar_pessoas(self):
        return self.pessoaDAO.listar()

    def buscar_pessoa(self, id):
        return self.pessoaDAO.buscarPorId(id)

    def atualizar_pessoa(self, novo_nome, novo_email, novo_telefone, novo_idade):
        atualizarPessoa = Pessoa(novo_nome, novo_email, novo_telefone, novo_idade)
        return self.pessoaDAO.criar(atualizarPessoa)

    def excluir_pessoa(self, id):
        return self.pessoaDAO.deletar_pessoa(id)