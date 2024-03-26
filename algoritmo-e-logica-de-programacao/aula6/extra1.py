a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

import math

delta = (b**2) - (4*a*c)

if delta < 0:
    print('Não tem solução')
else:
    x1 = -b + math.sqrt(delta) / 2*a
    x2 = -b - math.sqrt(delta) / 2*a
    print(f'''
        x1 = {x1:.2f}
        x2 = {x2:.2f}
    ''')