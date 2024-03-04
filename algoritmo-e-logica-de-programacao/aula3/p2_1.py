"""
Faça um programa que leia um valor em real
e mostre o equivalente em dólares
"""

real = float(input('Digite a quantidade em reais: '))

dolar = real / 4.95

print(f'O valor R${real:.2f}, convertido em dólares é de ${dolar:.2f}')