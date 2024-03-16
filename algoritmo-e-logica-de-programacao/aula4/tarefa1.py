"""
Crie um programa em Python que calcule a estimativa da população de uma cidade 
após um determinado número de anos.

O programa deve pedir ao usuário a população inicial e a taxa de 
crescimento anual (em porcentagem).

Em seguida, deve solicitar o número de anos para a projeção.
"""

populacao_inicial = int(input('Digite o valor inicial da população: '))
taxa_crescimento = float(input('Digite a taxa de crescimento em %: '))
projecao_anos = float(input('Digite o número de anos para a projeção: '))

populacao_futura = populacao_inicial * (1 + taxa_crescimento / 100) ** projecao_anos

print(f'A população estimada para {projecao_anos} anos é de {populacao_futura:.0f} habitantes')