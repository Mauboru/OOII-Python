class Pessoa:
    def __init__(self, id, nome, email, telefone, idade):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_email(self):
        return self.email

    def set_email(self, novo_email):
        self.email = novo_email

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def get_idade(self):
        return self.idade

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def get_id(self):
        return self.id
    
    def set_id(self, novo_id):
        self.id = novo_id

    # Método toString
    def __str__(self):
        return f"{self.nome}, {self.email}, {self.telefone}, {self.idade} anos"