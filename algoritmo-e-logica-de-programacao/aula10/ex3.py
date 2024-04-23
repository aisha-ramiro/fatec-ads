# Escreva um programa que imprima os primeiros 10 números da sequência de Fibonacci usando um laço FOR.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

print(f'''{a}
{b}''')

for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c