from Pessoa import Pessoa
from PessoaDAO import PessoaDAO
from Conexao import Conexao

class GerenciadorPessoas:
    def __init__(self, pessoaDAO):
        self.pessoaDAO = pessoaDAO

    def adicionar_pessoa(self, nome, email, telefone, idade):
        novaPessoa = Pessoa(nome, email, telefone, idade)
        return self.pessoaDAO.criar(novaPessoa)
        

    def listar_pessoas(self):
        return self.pessoaDAO.listar()

    def buscar_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                return pessoa
        return None

    def atualizar_pessoa(self, id, nome, nova_idade, nova_cidade):
        pessoa = self.buscar_pessoa(id)
        if pessoa:
            pessoa.idade = nova_idade
            pessoa.cidade = nova_cidade
            print(f"{nome} atualizado com sucesso.")
        else:
            print(f"{nome} não encontrado.")

    def excluir_pessoa(self, nome):
        pessoa = self.buscar_pessoa(nome)
        if pessoa:
            self.pessoas.remove(pessoa)
            print(f"{nome} removido com sucesso.")
        else:
            print(f"{nome} não encontrado.")