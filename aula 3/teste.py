class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome  # Propriedade nome do cachorro
        self.raca = raca  # Propriedade raça do cachorro

    def latir(self):
        return f"{self.nome} está latindo: Au Au!"

    def sentar(self):
        return f"{self.nome} está sentado."

# Criando um objeto a partir da classe Cachorro
meu_cachorro = Cachorro("Rex", "Labrador")

# Usando os métodos
print(meu_cachorro.latir())   # Saída: Rex está latindo: Au Au!
print(meu_cachorro.sentar())  # Saída: Rex está sentado.
