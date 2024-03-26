# Leia 2 notas (n1 e n2)
# - calcule a media
# media = (n1 + n2) / 2
# se media >= 7:
#   mostre('aprovado')
# senão:
# mostre('reprovado')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'A média do aluno foi de {media:.2f}: APROVADO')
else:
    print(f'A média do aluno foi de {media:.2f}: REPROVADO')
