#Faça um programa que leia o ano de nascimento
# calcule a idade = 2024 - ano

import datetime

data_atual = datetime.datetime.now()
ano_atual = data_atual.year

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade >= 18:
    print(f'O usuário tem {idade} anos e já pode tirar carteira de motorista!')
else:
    print(f'O usuário tem {idade} anos e ainda não pode tirar carteira de motorista!')
