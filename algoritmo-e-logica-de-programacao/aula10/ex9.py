#Faça um programa que leia a idade de 20 pessoas e exiba a soma das idades.

soma = 0

for i in range(20):
    idade = int(input('Digite a idade: '))
    soma += idade

print(f'A soma das idades = {soma}')