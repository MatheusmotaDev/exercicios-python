total_compra = float(input('Digite o valor total da sua compra: '))

desconto = 0

desconto = 0  
if total_compra >= 200:
    desconto = 0.20  
elif total_compra >= 100:
    desconto = 0.10  

    valor_final = total_compra * (1 - desconto)  

print(f"O valor final com desconto é: ${valor_final:.2f}")




