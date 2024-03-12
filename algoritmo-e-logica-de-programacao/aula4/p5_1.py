#Faça um programa que leia uma 
# temperatura em °C e converta para 
# °F e °K

temperatura_c = float(input('Digite a temperatura em °C: '))

temperatura_k = temperatura_c + 273
temperatura_f = 1.8 * temperatura_c + 32

print(f'''

! Boletim diário do clima !

Temperatura do dia:
    - {temperatura_c:.1f} °C
    - {temperatura_f:.1f} °F
    - {temperatura_k:.1f} °K

''')
