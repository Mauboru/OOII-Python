class Pessoa:
    def __init__(self, nome, email, telefone, idade):
        self._nome = nome
        self._email = email
        self._telefone = telefone
        self._idade = idade
        self._id = None

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_email(self):
        return self._email

    def set_email(self, novo_email):
        self._email = novo_email

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, novo_telefone):
        self._telefone = novo_telefone

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        self._idade = nova_idade

    def get_id(self):
        return self._id

    def set_id(self, novo_id):
        self._id = novo_id

    # Método toString
    def __str__(self):
        return f"Id :{self._id}, Nome:{self._nome}, Email:{self._email}, Telefone:{self._telefone}, Idade:{self._idade} anos"
