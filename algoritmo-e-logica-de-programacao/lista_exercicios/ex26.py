def decompor_valor_em_notas(valor):
    notas_100 = valor // 100
    valor %= 100
    notas_50 = valor // 50
    valor %= 50
    notas_10 = valor // 10
    valor %= 10
    notas_5 = valor // 5
    valor %= 5
    notas_1 = valor
    return notas_100, notas_50, notas_10, notas_5, notas_1

valor_em_reais = int(input("Digite o valor em reais: "))

notas_100, notas_50, notas_10, notas_5, notas_1 = decompor_valor_em_notas(valor_em_reais)

print(f"Valor lido: R$ {valor_em_reais}")
print("Notas necessárias:")
print("Notas de 100: ", notas_100)
print("Notas de 50: ", notas_50)
print("Notas de 10: ", notas_10)
print("Notas de 5: ", notas_5)
print("Notas de 1: ", notas_1)
