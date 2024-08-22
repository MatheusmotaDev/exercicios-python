nota_mat = int(input('Digite sua nota de matemática: '))
nota_prog = int(input('Digite sua nota de programação: '))



if nota_mat >= 60 and nota_prog >= 60:
     print ('Você foi aprovado')
elif nota_mat < 60 and nota_prog < 60:
     print ('Você foi reprovado')     