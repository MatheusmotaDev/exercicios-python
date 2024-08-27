# código simples para descobrir o número de vogais

palavra = input('Por favor, digite uma palavra: ')

vogal = 0

for char in palavra: 
    if char in "aeiouAEIOU":
        vogal += 1

print('Número de vogais:', vogal)         