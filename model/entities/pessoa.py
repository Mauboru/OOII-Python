class pessoa:
    def __init__(self, nome, email, telefone, idade):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade

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

    # Método toString
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.telefone}, {self.idade} anos"