# Faça um programa que leia o salário e 
# calcule o recebimento, sendo que: 
# - imposto = salario * 0.15
# - inss = salario * 0.17
# - recebimento = salario - imposto - inss

salario = float(input('Digite o seu salário: R$ '))

imposto = salario * 0.15
inss = salario * 0.17
recebimento = salario - imposto - inss 

print(f'''
O salário inicial é de R$ {salario:.2f}
Descontos:
Imposto - R$ {imposto:.2f}
INSS - R$ {inss:.2f}

Salário final - R$ {recebimento:.2f}
''')
