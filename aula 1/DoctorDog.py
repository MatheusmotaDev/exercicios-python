# exibição de uma clinica onde o usuário poderá descobrir a idade humana do seu cachorro

print('Clínica veterinária Doutor dog')

resp = input('Olá, seja bem vindo(a) a nossa cliníca, por favor digite seu nome: ')
dog = input('Agora digite o nome do seu cachorro para o prontuário: ')

idade = int(input('Digite a idade do seu cachorro: '))

calc = idade * 7

print(f'O responsável {resp} pelo cachorro {dog} tem o equivalente a {calc} anos humanos')