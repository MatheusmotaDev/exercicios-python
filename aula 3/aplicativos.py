# criando classes usando POO COM python
# modelo pessoa
# app rede social, app isotérico, app hospital


class PessoaClinica:
    def __init__(self, nome, idade, tipo_sangue, peso, altura):
        self.nome = nome
        self.idade = idade
        self.tipo_sangue = tipo_sangue
        self.peso = peso
        self.altura = altura

    def mostrar_informacoes(self):
        print(f"--- Cadastro na Clínica Médica ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Tipo Sanguíneo: {self.tipo_sangue}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print()


class PessoaEsoterica:
    def __init__(self, nome, idade, signo):
        self.nome = nome
        self.idade = idade
        self.signo = signo

    def mostrar_informacoes(self):
        print(f"--- Cadastro na Agência Esotérica ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Signo: {self.signo}")
        print()


class PessoaRedeSocial:
    def __init__(self, nome, idade, cor_olhos, hobbies, altura):
        self.nome = nome
        self.idade = idade
        self.cor_olhos = cor_olhos
        self.hobbies = hobbies
        self.altura = altura

    def mostrar_informacoes(self):
        print(f"--- Cadastro na Rede Social ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cor dos Olhos: {self.cor_olhos}")
        print(f"Hobbies: {self.hobbies}")
        print(f"Altura: {self.altura} m")
        print()


alex = PessoaClinica("Alex", 30, "O+", 75, 1.75)
maria = PessoaEsoterica("Maria", 28, "Virgem")
jonas = PessoaRedeSocial("Jonas", 25, "Castanho", "Leitura, Ciclismo", 1.80)


alex.mostrar_informacoes()
maria.mostrar_informacoes()
jonas.mostrar_informacoes()
