#Leia a hora e dia

hora = int(input('Digite a hora: '))
dia = input('Digite o dia da semana: ')

if hora > 6:
    if dia == 'Sábado':
        horaextra = 14.30
    else:
        horaextra = 11.10
else:
    if dia == 'Domingo':
        horaextra = 16.20
    else: 
        horaextra = 14.10

print(f'O valor da hora extra é de R${horaextra:.2f}')