# Exercicio 15

num = int(input('Digite um número: '))

if num % 2 == 0:
  print(f'O número {num} é par')
else:
  print(f'O número {num} é ímpar')

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")