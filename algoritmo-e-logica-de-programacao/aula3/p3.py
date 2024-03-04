'''
Faça um programa que: 
- Leia o tamanho de um lado de um quadrado
- Calcule a área = ladoxlado
- Mostre uma mensagem adequada
'''

lado = float(input("Qual é o lado do quadrado em cm? "))

area = lado * lado

print(f'Um quadrado de lado {lado:.1f} cm tem {area:.1f} cm de area ')