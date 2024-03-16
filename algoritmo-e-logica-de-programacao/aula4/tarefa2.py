"""
Escreva um programa que solicite ao usuário um valor inicial, 
uma taxa de juros anual e o número de anos. 

O programa deve calcular e exibir o valor futuro após o período especificado
"""

valor_inicial = float(input('Insira o valor inicial: R$ '))
taxa_juros = float(input('Insira a taxa de juros anual: '))
anos = float(input('Insira o período desejado em anos: '))

valor_futuro = valor_inicial * (1 + taxa_juros / 100) ** anos

print(f'''
  Valor inicial: R${valor_inicial:.2f};
  Taxa de juros: {taxa_juros}%;
  Período: {anos} anos.

  Valor futuro: R${valor_futuro:.2f}.
''')