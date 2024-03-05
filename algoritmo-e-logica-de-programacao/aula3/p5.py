'''
Faça um programa que:
-Leia do usuário a quantidade de horas trabalhadas
- Calcule o salário, sabendo que cada hora vale 87.50
'''

horas = float(input('Digite o número de horas trabalhadas: '))
salario = horas * 87.50

print(f'O funcionário trabalhou {horas:.2f} e receberá um salário de R${salario:.2f}')