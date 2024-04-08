# Exercicio 5

from datetime import datetime

idade = int(input('Digite a sua idade em dias: '))

anos = idade / 365
meses = anos * 12

print(f'A idade de {idade} dias, é igual a {meses:.0f} meses ou {anos:.0f} anos')


