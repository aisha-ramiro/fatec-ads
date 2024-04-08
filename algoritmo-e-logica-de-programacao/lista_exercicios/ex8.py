# Exercicio 8

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))
e = float(input('Digite o valor de e: '))
f = float(input('Digite o valor de f: '))

x = (c * e) - (b * f) / (a * e) - (b * d)
y = (a * f) - (c * d) / (a * e) - (b * d) 

print(f'X = {x:.2f} e Y = {y:.2f}')