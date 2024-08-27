# criando classes usando POO COM python
# modelo pessoa
# app rede social, app isotérico, app hospital

from decimal import Decimal

class Pessoa:
    def __init__(self, nome, identificacao, nacionalidade):
        self.nome = nome
        self.identificacao = identificacao
        self.nacionalidade = nacionalidade


