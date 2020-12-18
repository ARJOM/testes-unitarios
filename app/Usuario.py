import hashlib


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.senha = hashlib.md5(senha.encode()).hexdigest()
        self.email = email
        self.opnioes = {}

    def add_opniao(self, chave, valor):
        self.opnioes[chave] = valor

    def verifica_senha(self, senha):
        return hashlib.md5(senha.encode()).hexdigest() == self.senha 
