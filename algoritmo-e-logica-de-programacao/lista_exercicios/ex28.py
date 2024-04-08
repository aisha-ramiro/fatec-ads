def calcular_duracao_jogo(hora_inicio, minuto_inicio, hora_termino, minuto_termino):
    inicio_minutos = hora_inicio * 60 + minuto_inicio
    termino_minutos = hora_termino * 60 + minuto_termino

    if termino_minutos < inicio_minutos:
        termino_minutos += 24 * 60

    duracao_minutos = termino_minutos - inicio_minutos

    duracao_horas = duracao_minutos // 60
    duracao_minutos %= 60

    return duracao_horas, duracao_minutos

hora_inicio = int(input("Digite a hora de início do jogo: "))
minuto_inicio = int(input("Digite os minutos de início do jogo: "))

hora_termino = int(input("Digite a hora de término do jogo: "))
minuto_termino = int(input("Digite os minutos de término do jogo: "))

duracao_horas, duracao_minutos = calcular_duracao_jogo(hora_inicio, minuto_inicio, hora_termino, minuto_termino)

print("Duração do jogo:", duracao_horas, "horas e", duracao_minutos, "minutos")
