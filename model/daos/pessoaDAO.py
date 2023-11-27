import conexao
from entities import Pessoa
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

                pessoa_id = cursor.lastrowid

                return f"{Fore.GREEN}Pessoa inserida com sucesso.{Fore.RESET}"

                
        except Exception as e:
            return f"{Fore.RED}Erro ao inserir pessoa: {e}{Fore.RESET}"

    def listar(self):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''SELECT * FROM pessoa''')
                
                pessoas = []
                
                for row in cursor.fetchall():
                    pessoa = Pessoa(id=row[0], nome=row[1], email=row[2], telefone=row[3], idade=row[4])
                    pessoas.append(pessoa)
                
                return pessoas
        except Exception as e:
            print(f"{Fore.RED}Erro ao listar pessoas: {e}{Fore.RESET}")
            return []
        
    def atualizar(self, pessoa):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''
                    UPDATE pessoa SET nome = ?, email = ?, telefone = ?, idade = ? WHERE id= ?
                ''', (pessoa.nome, pessoa.email, pessoa.telefone, pessoa.idade, pessoa.id))
                return f"{Fore.GREEN}Pessoa atualizada com sucesso.{Fore.RESET}"
        except Exception as e:
            return f"{Fore.RED}Erro ao atualizar pessoa: {e}{Fore.RESET}"

    def deletar_pessoa(self, pessoa_id):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('DELETE FROM pessoa WHERE id = ?', (pessoa_id))
                return f"{Fore.GREEN}Pessoa deletada com sucesso.{Fore.RESET}"
        except Exception as e:
            return f"{Fore.RED}Erro ao deletar pessoa: {e}{Fore.RESET}"      