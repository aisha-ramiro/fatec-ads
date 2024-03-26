#Fazer um programa que leia a idade e mostre:
# Se idade > 17:
# mostra('Maior de idade')
# senão:
# mostra ('Menor de idade')

idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print(f'O usuário tem {idade} anos, portanto é maior de idade. ')
else:
    print(f'O usuário tem {idade} anos, portanto é menor de idade.')