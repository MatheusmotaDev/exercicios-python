from datetime import datetime

print('Bem vindo ao adivinhador de idade!')

nome = input('Para começarmos, digite o seu nome: ')
ano = int(input('Agora digite o ano do seu nascimento: '))

ano_atual = datetime.now().year

calc = ano_atual - ano

print(f'Descobri sua idade {nome}! você tem {calc} anos :) ')