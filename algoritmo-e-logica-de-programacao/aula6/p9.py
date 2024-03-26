#Leia um número
# número > 0
# calcule e mostre a raiz quadrada
# senão
# mostre que nao há raiz

import math

numero = float(input('Digite um número: '))

if numero > 0:
    raiz = math.sqrt(numero)
    print(f'A raiz quadrada de {numero:.2f} é igual a {raiz:.2f}')
else: 
    print(f'Não há raiz de para esse número')