# Faça um programa que leia os valores
# e calcule a area de um trapézio


base_maior = float(input('Digite o valor da base maior em centímetros: '))
base_menor = float(input('Digite o valor da base menor em centímetros: '))
altura = float(input('Digite o valor da altura em centímetros: '))

area = (base_maior + base_menor / 2) * altura

print(f'A área do trapézio é de {area}cm')
