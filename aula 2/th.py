import random

numero_aleatorio = random.randint(1, 100)

adv = int(input('Por favor, digite um número: '))

while adv != numero_aleatorio:
  
  if numero_aleatorio > adv:
     print ('o número é maior')
     adv = int(input('Por favor, digite um número: '))
     

  elif numero_aleatorio < adv:
     print ('o número é menor')  
     adv = int(input('Por favor, digite um número: '))
  

print ('Parabéns!')   