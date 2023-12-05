from model.entities.Pessoa import Pessoa

class RepositorioPessoa:
    def __init__(self, pessoaDAO):
        self.pessoaDAO = pessoaDAO

    def adicionar_pessoa(self, nome, email, telefone, idade):
        if nome == "" or email == "" or telefone == "" or idade is None:
            return ValueError("Nenhuma das variáveis pode ser nula")

        nova_pessoa = Pessoa(nome, email, telefone, idade)
        return self.pessoaDAO.criar(nova_pessoa)

    def listar_pessoas(self):
        return self.pessoaDAO.listar()

    def buscar_pessoa(self, id):
        return self.pessoaDAO.buscarPorId(id)

    def atualizar_pessoa(self, id, novo_nome, novo_email, novo_telefone, novo_idade):
        if novo_nome == "" or novo_email == "" or novo_telefone == "" or novo_idade is None:
            return ValueError("Nenhuma das variáveis pode ser nula")

        pessoa_atualizada = Pessoa(novo_nome, novo_email, novo_telefone, novo_idade, id)
        return self.pessoaDAO.atualizar(pessoa_atualizada)

    def excluir_pessoa(self, id):
        return self.pessoaDAO.deletar_pessoa(id)
