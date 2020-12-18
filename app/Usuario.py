class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.opnioes = {}

    def add_opniao(self, chave, valor):
        self.opnioes[chave] = valor
