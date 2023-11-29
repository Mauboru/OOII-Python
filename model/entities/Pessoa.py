class Pessoa:
    def __init__(self, id, nome, email, telefone, idade):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__idade = idade
        self.__id = id

    def __init__(self, nome, email, telefone, idade):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_email(self):
        return self.__email

    def set_email(self, novo_email):
        self.__email = novo_email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    def get_id(self):
        return self.__id

    def set_id(self, novo_id):
        self.__id = novo_id

    # Método toString
    def __str__(self):
        return f"Id : {self.__id}, \nNome: {self.__nome}, \nEmail: {self.__email}, \nTelefone: {self.__telefone}, \nIdade: {self.__idade} anos\n"