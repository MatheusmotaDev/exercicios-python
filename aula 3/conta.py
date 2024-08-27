# criando classes usando POO COM python
# visualizando informações de uma conta bancária


from decimal import Decimal


class Pessoa:
    def __init__(self, nome, identificacao, nacionalidade):
        self.nome = nome
        self.identificacao = identificacao
        self.nacionalidade = nacionalidade

    def mostrar_informacoes(self):
        print(f"--- Informações do Titular ---")
        print(f"Nome: {self.nome}")
        print(f"Identificação: {self.identificacao}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print()


class ContaBancaria:
    def __init__(self, titular, saldo, tipo_conta, tipo_moeda):
        self.titular = titular  
        self.saldo = Decimal(saldo)  
        self.tipo_conta = tipo_conta
        self.tipo_moeda = tipo_moeda

    def mostrar_informacoes(self):
        print(f"--- Informações da Conta Bancária ---")
        self.titular.mostrar_informacoes()  
        print(f"Saldo: {self.saldo} {self.tipo_moeda}")
        print(f"Tipo de Conta: {self.tipo_conta}")
        print(f"Tipo de Moeda: {self.tipo_moeda}")
        print()


titular = Pessoa("Matheus Alves", "25102004", "Brasileiro")


conta = ContaBancaria(titular, 1000.50, "Conta Corrente", "Reais")


conta.mostrar_informacoes()
