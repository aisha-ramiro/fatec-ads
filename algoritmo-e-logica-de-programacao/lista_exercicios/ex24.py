def calcular_duracao_jogo(inicio, fim):
    duracao = fim - inicio
    if duracao < 0:
        duracao += 24
    return duracao

inicio = int(input("Digite a hora de início do jogo: "))
fim = int(input("Digite a hora do final do jogo: "))

duracao_jogo = calcular_duracao_jogo(inicio, fim)

print("A duração do jogo em horas é:", duracao_jogo)
