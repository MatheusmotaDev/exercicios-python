saldo = 100

print('BEM VINDO AO BANCO MUNDIAL')
nome = input('Para continuar, digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 17:
    print('Você não está autorizado ao usar nossos serviços')
    exit()
else:
    print(f'Olá {nome}, seja bem vindo ao nosso banco, ao prosseguir, você aceitou aos nossos termos de serviço')






while True:
    print('Opcões: ')
    print('1 - depósito ')
    print('2 - Saque')
    print('3 - consultar saldo')
    print('4 - sair')

    escolha = int(input('Digite a opção que você desejar: '))

    if escolha == 1:
        deposito = float(input('Digite o valor do depósito: '))
        saldo += deposito
        print (f"Depósito realizado com sucesso! seu saldo é de {saldo:2f}")
    elif escolha == 2:
        saque = float(input('Digite o valor que deseja sacar: '))
        saldo -= saque
        print(f'você sacou {saque}, seu saldo atual é de {saldo:.2f}')
    elif escolha == 3:
        print(f'Saldo atual {saldo:.2f} R$')
    elif escolha == 4:
        break
   
  
    

