# gerador de email simples a partir do seu nome

print("Seja bem vindo ao novo criador de e-mail")

nome = input('Por favor, digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ').lower()

inicial = nome[0].lower()

prox = input('Email criado! por favor, digite qualquer tecla para visualizar seu novo e-mail ->')

print(f'Seu novo email é {inicial}{sobrenome}@gmail.com')