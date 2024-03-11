# Faça um programa que leia os dados necessários 
# de um cone e calcule a area

import math

raio = float(input('Digite o raio do cone: '))
altura = float(input('Digite a altura do cone: '))
pi = 3.14

geratriz = math.sqrt(raio**2 + altura**2) 

area_total = pi * raio * (geratriz + raio)


print(f'A área total do cone é de {area_total:.2f} centímetros')