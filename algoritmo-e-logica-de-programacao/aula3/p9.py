'''
Faça um programa que leia
-Cateto oposto
-Cateto adjacente

Calcule a hipotenusa
hipotenusa = 

'''

import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hipotenusa = math.sqrt(co ** 2 + ca **2)

print(f'O valor da hipotenusa é = {hipotenusa:.2f}')
