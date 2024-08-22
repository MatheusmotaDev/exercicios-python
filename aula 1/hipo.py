import math

print('Calculadora avançada de hipotenusa')

a = float(input('Digite o número do cateto A: '))
b = float(input('Digite o número do cateto B: '))

hipotenusa = math.sqrt(a**2 + b**2)

print(f" a hipotenusa é {hipotenusa:.2f}")