# Código simples para conversão de moedas internacionais

print('Empresa de câmbio internacional')

nome = input('Olá, para fins de segurança, informe seu nome: ')

dolar = float(input('Digite a quantidade de dólares que deseja converter: '))
taxa_cambio = float(input('Digite a taxa de câmbio atual (1 dólar em euros): '))

calc = dolar * taxa_cambio

print(f'A operação do usuário {nome} foi finalizada com sucesso! {dolar} doláres foram convertidos em {calc} euros')

