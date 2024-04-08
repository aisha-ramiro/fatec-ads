# Exercicio 12

idade = int(input('Digite a idade do nadador: '))

if idade >= 5 and idade <= 7:
  classificacao = 'Infantil A'
elif idade >= 8 and idade <= 10:
    classificacao = 'Infantil B'
elif idade >= 11 and idade <= 13:
    classificacao = 'Juvenil A'
elif idade >= 14 and idade <= 17:
    classificacao = 'Juvenil B'
elif idade >= 18:
    classificacao = 'Adulto'
else:
    classificacao = 'Idade indisponível'

print(classificacao)