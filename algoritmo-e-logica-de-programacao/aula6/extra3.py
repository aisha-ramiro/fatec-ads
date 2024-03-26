total = float(input('Digite o valor total da compra: R$ '))

def calculo_desconto(total, desconto):
    valor_desconto = total * desconto
    valor_final = total - valor_desconto
    print(f'''
    Você ganhou um desconto de {desconto} %

    Valor da compra: R$ {total:.2f}
    Valor do desconto: R$ {valor_desconto:.2f}
    Valor final: R$ {valor_final:.2f}
    ''')

if total > 100:
    calculo_desconto(total, 0.15)
else: 
    calculo_desconto(total, 0.08)
