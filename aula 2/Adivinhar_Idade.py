# código para adivinhar a a faixa etária do indivíduo

nome = input("Olá, digite seu nome: ")

idade = int(input("Digite sua idade atual: "))


if   idade >= 0 and idade <= 12:
    print (f' oi {nome} Você é criança')
elif idade >= 13 and idade <= 17:
      print (f' oi {nome} Você é adolescente')    
elif idade >= 18 and idade <= 64:
     print (f' oi {nome} Você é adulto')
elif idade >= 65:
      print (f' oi {nome} Você Você é idoso')          
