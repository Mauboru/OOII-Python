import conexão
from entities import pessoa
from colorama import Fore

class pessoaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def criar(self, pessoa):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''
                    INSERT INTO pessoa (nome, email, telefone, idade)
                    VALUES (?, ?, ?, ?)
                ''', (pessoa.nome, pessoa.email, pessoa.telefone, pessoa.idade))
                print(f"{Fore.GREEN}Pessoa inserida com sucesso.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Erro ao inserir pessoa: {e}{Fore.RESET}")

    def listar(self):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''SELECT * FROM pessoa''', (pessoa.nome, pessoa.email, pessoa.telefone, pessoa.idade))
                print(f"{Fore.GREEN}Pessoas listadas com sucesso.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Erro ao listar pessoas: {e}{Fore.RESET}")   

    def deletar_pessoa(self, pessoa_id):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('DELETE FROM pessoa WHERE id = ?', (pessoa_id,))
                print(f"{Fore.GREEN}Pessoa deletada com sucesso.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Erro ao deletar pessoa: {e}{Fore.RESET}")
  