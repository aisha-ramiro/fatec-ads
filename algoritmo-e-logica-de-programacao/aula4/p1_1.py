"""
Faça um programa que resolva a fórmula de báscara\
    leia a, b, c
    depois calcule o delta
    depois calcule x1 e x2
"""



a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (b**2) - (4*a*c)

raiz_delta = delta**0.5

x1 = (-b + raiz_delta) / (2*a)
x2 = (-b - raiz_delta) / (2*a)

print(f'O resultado de x1 = {x1:.2f} e x2 = {x2:.2f}')