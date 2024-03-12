#Faça um programa que leia o 
# valor da compra e:
# - Calcule o juros = valor * 0.12
# - Calcule a multa = valor * 0.09
# - Calcule o desconto = valor * 0.10
# Mostre o total = valor + juros + multa - desconto

compra = float(input("Qual foi o valor da compra? R$ "))
juros = compra * 0.12
multa = compra * 0.09
desconto = compra * 0.10

total = compra + juros + multa - desconto

print(f"""

Valor total da compra: R$ {total:.2f}

    Detalhes:
    - Valor da compra: R$ {compra:.2f}
        Acréscimos:
        - Juros: {juros:.2f}
        - Multa: {multa:.2f}
        Decréscimos:
        - Desconto especial: {desconto:.2f}

""")