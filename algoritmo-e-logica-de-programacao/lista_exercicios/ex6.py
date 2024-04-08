#Exercicio 6

segundos = int(input("Digite o tempo de duração do evento em segundos: "))

horas = segundos / 3600
minutos = (segundos % 3600) / 60
segundos = segundos % 60

print(f"O evento dura {horas:.0f} horas, {minutos:.0f} minutos e {segundos:.0f} segundos.")
