#Escreva um programa que leia do usuário um valor em real
#e converta para euro, dólar, ien, peso

real = float(input("Digite o valor em real: R$"))

dolar = real/4.98
euro = real/5.44
iene = real/0.034
peso = real/0.3

print(f"""
O valor de R$ {real}, convertido em:
    - Euro: €{euro:.2f}
    - Dólar: ${dolar:.2f}
    - Iene: ¥{iene:.2f}
    - Peso: ${peso:.2f}
""")