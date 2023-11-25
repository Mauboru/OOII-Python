import conexão
from entities import pessoa


class pessoaDAO:
    def __init__(self, conexao):
        self.conexao = conexao