import sqlite3 as sql
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_banco_dados():
    try:
        with sql.connect(os.getenv("DB_NAME", "sqlite.db")) as conexao:
            cursor = conexao.cursor()
            return conexao, cursor
    except sql.Error as e:
        return "Erro ao conectar ao banco de dados"
