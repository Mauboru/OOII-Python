from model.daos.Conexao import Conexao
from model.entities.Pessoa import Pessoa
from colorama import Fore
import sqlite3 as sql

class PessoaDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def criar(self, pessoa):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''
                    INSERT INTO pessoa (nome, email, telefone, idade)
                    VALUES (?, ?, ?, ?)
                ''', (pessoa.get_nome(), pessoa.get_email(), pessoa.get_telefone(), pessoa.get_idade()))

                return f"{Fore.GREEN}Pessoa inserida com sucesso.{Fore.RESET}"                
        except sql.Error as e:
            return f"{Fore.RED}Erro ao inserir pessoa: {e}{Fore.RESET}"

    def listar(self):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''SELECT * FROM pessoa''')
                
                pessoas = []
                
                for row in cursor.fetchall():
                    pessoa = Pessoa(nome=row[1], email=row[2], telefone=row[3], idade=row[4])
                    pessoa.set_id(row[0])
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
                ''', (pessoa.get_nome(), pessoa.get_email(), pessoa.get_telefone(), pessoa.get_idade(), pessoa.get_id()))
                
                return f"{Fore.GREEN}Pessoa atualizada com sucesso.{Fore.RESET}"
        except sql.Error as e:
            return f"{Fore.RED}Erro ao atualizar pessoa: {e}{Fore.RESET}"

    def deletar_pessoa(self, id):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''DELETE FROM pessoa WHERE id = ?''', (id,))

                return f"{Fore.GREEN}Pessoa deletada com sucesso.{Fore.RESET}"
        except Exception as e:
            return f"{Fore.RED}Erro ao deletar pessoa: {e}{Fore.RESET}"      
        
    def buscarPorId(self, id):
        try:
            with self.conexao:
                cursor = self.conexao.cursor()
                cursor.execute('''SELECT * FROM pessoa WHERE id = ?''', (id,))
                
                row = cursor.fetchone()

                if row:
                    pessoa = Pessoa(nome=row[1], email=row[2], telefone=row[3], idade=row[4])
                    pessoa.set_id(row[0])

                    return pessoa
        except Exception as e:
            print(f"{Fore.RED}Erro ao buscar pessoa: {e}{Fore.RESET}")
            return None