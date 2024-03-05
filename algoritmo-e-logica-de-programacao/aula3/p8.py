'''
Faça um programa que:
- Calcule o investimento
-Leia do usuário:
    - valor
    - juros
    - periodo

- Calcule o valor final:
(valor * (1 + juros/100)) ** periodo
'''

valor = float(input('Digite o valor: '))
juros = float(input('Digite a taxa de juros: '))
periodo = float(input('Digite o período: '))

valor_final = valor * (1 + juros/100)** periodo 

print(f'O valor do investimento é de: {valor_final:.2f}')

