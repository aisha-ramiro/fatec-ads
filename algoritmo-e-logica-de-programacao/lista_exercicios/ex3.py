#Exercicio 3

from datetime import datetime

idade = (input('Digite a sua data de nascimento no formato dd/mm/aaaa: '))
idade = datetime.strptime(idade, "%d/%m/%Y")

data_atual = datetime.now()

diferenca = data_atual - idade

dias = diferenca.days

print(f'Você tem {dias} dias')