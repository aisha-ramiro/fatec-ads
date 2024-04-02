# Crie um programa que leia um valor da nota fiscal e série da nota

valor = float(input('Digite o valor da nota fiscal: '))
serie = input('Digite a série da nota: ')

if serie == 'B1':
    if valor < 100:
        imposto = valor * 0.08
    else:
        imposto = valor * 0.12
else:
    imposto = valor * 0.18 

print(f'''
    Nota de valor {valor} e série {serie}
    Imposto: {imposto:.2f}
    Total: {valor + imposto}
''')