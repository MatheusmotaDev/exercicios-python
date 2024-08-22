lado_1 = float(input("Digite o comprimento do primeiro lado: "))
lado_2 = float(input("Digite o comprimento do segundo lado: "))
lado_3 = float(input("Digite o comprimento do terceiro lado: "))

if lado_1 == lado_2 == lado_3:
    print("O triângulo é equilátero.")
elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
