print('Calculadora IMC')

peso = float(input('Digite seu peso em quilogramas: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

print(f'Seu imc é de {imc:.2f}')
