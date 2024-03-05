'''
Faça um programa que:
-Leia a distância
-Leia o tempo
Calcule a velocidade média
media = velocidade/tempo
'''

distancia = float(input('Digite a distância em metros: '))
tempo = float(input('Digite o tempo em minutos: '))

velocidade = distancia / tempo 

print(f'A velocidade média é igual a {velocidade:.2f} metros por minuto')