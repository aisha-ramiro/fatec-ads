def calcular_media_aritmetica(notas):
    return sum(notas) / len(notas)

def calcular_media_ponderada(notas):
    return (notas[0]*3 + notas[1]*3 + notas[2]*4) / 10

def calcular_media_harmonica(notas):
    return len(notas) / sum(1/nota for nota in notas)

notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(3)]
opcao = int(input("Escolha o tipo de média a ser calculada:\n1 - Aritmética\n2 - Ponderada\n3 - Harmônica\nOpção: "))

if opcao == 1:
    media = calcular_media_aritmetica(notas)
    print("A média aritmética é:", media)
elif opcao == 2:
    media = calcular_media_ponderada(notas)
    print("A média ponderada é:", media)
elif opcao == 3:
    media = calcular_media_harmonica(notas)
    print("A média harmônica é:", media)
else:
    print("Opção inválida!")
