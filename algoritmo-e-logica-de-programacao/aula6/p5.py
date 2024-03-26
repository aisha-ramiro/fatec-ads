#Faça um programa que leia o total
# se total > 100
#   mostra ('Desconto de 15%)
# senão:
#   mostra('Desconto de 8%)

total = float(input('Digite o valor total da compra: R$ '))

if total > 100:
    print('Você ganhou um desconto de 15%')
else: 
    print('Você ganhou um desconto de 8%')