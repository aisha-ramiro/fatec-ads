#Crie um programa que leia do usuário 1 número
# e mostrea raiz quadrada deste número

import math

numero = int(input("Digite um número: "))
raiz_quadrada = math.sqrt(numero)

print(f'A raiz quadrada do número {numero} é {raiz_quadrada:.1f}')