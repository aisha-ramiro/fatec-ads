n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2 
subt = n1 - n2
mult = n1 * n2 
divi = n1 / n2 

print(f'''
Soma: {n1} + {n2} = {soma};
Subtração: {n1} - {n2} = {subt};
Multiplicação: {n1} * {n2} = {mult};
Divisão: {n1} / {n2} = {divi:.1f};
''')