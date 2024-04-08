def ordenar_crescente(a, b, c):
    return sorted([a, b, c])

def ordenar_decrescente(a, b, c):
    return sorted([a, b, c], reverse=True)

def colocar_maior_no_meio(a, b, c):
    maior = max(a, b, c)
    menor = min(a, b, c)
    meio = (a + b + c) - maior - menor
    return maior, meio, menor

i = int(input("Digite o valor de i (1, 2 ou 3): "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if i == 1:
    resultado = ordenar_crescente(a, b, c)
    print("Em ordem crescente:", resultado)
elif i == 2:
    resultado = ordenar_decrescente(a, b, c)
    print("Em ordem decrescente:", resultado)
elif i == 3:
    resultado = colocar_maior_no_meio(a, b, c)
    print("Maior valor no meio:", resultado)
else:
    print("Valor de i inválido. Por favor, escolha 1, 2 ou 3.")
