'''
Faça um programa que:
-Leia a nota de trabalho
-Leia a nota da prova
-Leia a nota do tcc
-Calcule a media=
trabalho*0.2
prova*0.5
tcc*0.3
'''

trabalho = float(input('Digite a nota do trabalho: '))
prova = float(input('Digite a nota da prova: '))
tcc = float(input('Digite a nota do tcc: '))

media = (trabalho*0.2) + (prova*0.5) + (tcc*0.3)

print(f'A média final do aluno foi de: {media:.1f}')