# criando classes usando POO COM python
# lojinha utilizando POO e outros recursos e também adição de descontos

class CarroBrinquedo:
    def __init__(self, nome, modelo, cor, preco, disponibilidade, tipo_controle, personagem=None):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.tipo_controle = tipo_controle
        self.personagem = personagem

    def mostrar_informacoes(self):
        print(f"--- Informações do Carrinho ---")
        print(f"Nome: {self.nome}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Disponibilidade: {'Em estoque' if self.disponibilidade else 'Indisponível'}")
        print(f"Tipo de Controle: {self.tipo_controle}")
        if self.personagem:
            print(f"Personagem: {self.personagem}")
        print()

    def verificar_disponibilidade(self):
        return self.disponibilidade

    def aplicar_desconto(self, percentual):
        if 0 < percentual < 100:
            desconto = self.preco * (percentual / 100)
            self.preco -= desconto
        else:
            print("Desconto inválido!")



carro1 = CarroBrinquedo("Carrinho do Mario Bros", "Manual", "Vermelho", 150.00, True, "Manual", "Mario")
carro2 = CarroBrinquedo("Carrinho Vermelho de Controle Remoto", "Simples", "Vermelho", 120.00, True, "Controle Remoto")
carro3 = CarroBrinquedo("Carrinho 4x4 Azul", "4x4", "Azul", 200.00, False, "Controle Remoto")
carro4 = CarroBrinquedo("Carrinho 4x4 Azul e Preto", "4x4", "Azul e Preto", 220.00, True, "Controle Remoto")


carro1.mostrar_informacoes()
carro2.mostrar_informacoes()
carro3.mostrar_informacoes()
carro4.mostrar_informacoes()


if carro1.verificar_disponibilidade():
    print(f"Aplicando 10% de desconto ao {carro1.nome}")
    carro1.aplicar_desconto(10)
    carro1.mostrar_informacoes()
