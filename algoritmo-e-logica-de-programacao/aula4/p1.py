"""
Crie um programa que leia do usuário:
- número
- expoente

mostre o reultado de número elevado ao expoente
ex: resultado = numero**expoente
"""

numero = float(input("Digite o número: "))
expoente = int(input("Digite o expoente: "))

resultado = numero**expoente

print(f'O número {numero} elevado a {expoente} é igual a {resultado:.2f}')