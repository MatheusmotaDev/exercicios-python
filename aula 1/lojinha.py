# demonstração de uma pequena loja em python 
# a compra sempre terá 10% de desconto

print('Olá! seja bem vindo a loja futurama! ')

nome = input('Por favor, antes de navegar no sistema, informe seu nome: ')

print(f'Olá {nome}, seja bem vindo a melhor loja do brasil !')

produto = input('Informe o produto que você deseja: ')

print (f'Você selecionou comprar {produto}')
prox = input('Pressione qualquer tecla para finalizar a compra ->')

total_compra = float(input('Digite o valor total da compra em R$: '))

print('Parabéns! você recebeu um desconto de 10% na sua compra')
nxt = input('Pressione qualquer tecla para avançar ->')

desconto_total = total_compra - (total_compra * 0.10)

print (f'O valor total da sua compra {total_compra} R$ recebeu um desconto de 10% e o valor final ficou em {desconto_total:.2f} R$')





