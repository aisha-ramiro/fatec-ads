#Crie um programa que leia a idade e altura 

idade = int(input('Digite a sua idade: '))
altura = int(input('Digite a sua altura em cm: '))

if idade > 17: 
    if altura > 180:
        bolsa = 1450
    else:
        bolsa = 1670
else:
    bolsa = 1433

print(f'O valor da bolsa é de R$ {bolsa}')

