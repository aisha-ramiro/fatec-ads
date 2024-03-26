# Faça um programa que leia (x1, y1) e (x2, y2)
# Calcule inclinacao 
# se inclinaçao > 1 
#   calcule z = inclinação * 0.9
# senao
#   calcule z = inclinacao * 1.8

import math

x1 = float(input('Digite o valor de x1: '))
y1 = float(input('Digite o valor de y1: '))
x2 = float(input('Digite o valor de x2: '))
y2 = float(input('Digite o valor de y2: '))

inclinacao = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if inclinacao > 1:
    z = inclinacao * 0.9
    print(f'O resultado é {z:.2f}')
else:
    z = inclinacao * 1.8
    print(f'O resultado é {z:.2f}')
