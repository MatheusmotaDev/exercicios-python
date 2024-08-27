# código simples para calcular seu índice de massa corporal

print('Calculadora IMC')

nome = input('Olá, digite seu nome: ')

peso = float(input('Digite seu peso em quilogramas: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)



if imc >= 0 and imc <= 18.5:
    print('Abaixo do normal, procure um nutricionista')
elif imc >= 18.6 and imc <= 24.5:
    print('Normal, você está saudável')    
elif imc >= 24.6 and imc <= 29.9:
    print('Você está com sobrepeso!')    
elif imc >= 30 and imc <= 34.5:
    print('ALERTA! Você está em OBESIDADE GRAU 1')  
elif imc >= 35 and imc <= 39.9:
    print('Você está em OBESIDADE GRAU 2 !')      
elif imc >= 40:
    print('Você está em OBESIDADE GRAU 3')
    print('Por favor, procure um médico urgente')    



print(f'{nome} Seu imc é de {imc:.2f}')