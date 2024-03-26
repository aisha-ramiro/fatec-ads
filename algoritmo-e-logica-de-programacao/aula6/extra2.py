#Leia o salário e calcule o imposto IR
# se salario < 1500
#   imposto = 5%
# se salario >= 1500 e salario < 2100
#   imposto 12%
# senão
#   imposto = 18%

salario = float(input('Digite o valor do salário: R$'))

def calcular_imposto(taxa, salario):
    valor_imposto = salario * taxa
    valor_salario = salario - valor_imposto

    return valor_imposto, valor_salario

if salario < 1500:
    valor_imposto, valor_salario = calcular_imposto(0.05, salario)
    print(f'''
        Salário: R${salario:.2f}
        Imposto 5%: R${valor_imposto:.2f}
        Valor final: R${valor_salario:.2f}
    ''')
elif salario >= 1500 and salario < 2100:
    imposto = salario * 0.12
    salario_final = salario - imposto
    print(f'''
        Salário: R${salario:.2f}
        Imposto 12%: R${imposto}
        Valor final: R${salario_final}
    ''')
else:
    imposto = salario * 0.18
    salario_final = salario - imposto
    print(f'''
        Salário: R${salario:.2f}
        Imposto 18%: R${imposto}
        Valor final: R${salario_final}
    ''')