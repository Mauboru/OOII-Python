import sqlite3 as sql
import os
from dotenv import load_dotenv

class Conexao:
    load_dotenv()
    
    @staticmethod
    def conectar_banco_dados():
        try:
            conexao = sql.connect(os.getenv("DB_NAME", "sqlite.db"))
            return conexao
        except sql.Error as e:
            raise ConnectionError(f"Erro ao conectar ao banco de dados: {e}")
    
