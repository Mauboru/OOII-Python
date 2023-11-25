from entities import pessoa
from daos import pessoaDAO

class GerenciadorPessoas:
    def __init__(self):
        self.pessoas = []
        

    def adicionar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        

    def listar_pessoas(self):
        for pessoa in self.pessoas:
            print(pessoa)

    def buscar_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                return pessoa
        return None

    def atualizar_pessoa(self, nome, nova_idade, nova_cidade):
        pessoa = self.buscar_pessoa(nome)
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