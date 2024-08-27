# código simples para descobrir se a pessoa foi ou não foi aprovada



nome = input('Digite o nome do aluno: ')

nota_mat = float(input('Digite sua nota de matemática: '))
nota_prog = float(input('Digite sua nota de programação: '))



if nota_mat >= 60 and nota_prog >= 60:
     print (f'{nome}, Você foi aprovado')
elif nota_mat < 60 and nota_prog < 60:
     print (f' {nome}, Você foi reprovado')     