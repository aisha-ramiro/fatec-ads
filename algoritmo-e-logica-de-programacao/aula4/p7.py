# Faça um programa que leia os catetos e
# calcule a hipotenusa

import math

ca = float(input("Qual o valor do cateto adjascente? "))
co = float(input("Qual o valor do cateto oposto? "))

hipotenusa = math.sqrt(ca**2 + co**2)

print(f'O valor da hipotenusa é {hipotenusa:.2f}')
