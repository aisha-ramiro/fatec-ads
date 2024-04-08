#Exercicio 11

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a % b == 0:
    print(f"{a} é múltiplo de {b}.")
elif b % a == 0:
    print(f"{b} é múltiplo de {a}.")
else:
    print(f"{a} e {b} não são múltiplos um do outro.")