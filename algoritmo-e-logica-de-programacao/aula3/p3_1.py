'''
Área do triângulo

- Faça um programa que leia os valores e calcule
a área do triângulo

'''

largura = float(input('Digite a largura do triângulo em cm: '))
altura = float(input('Digite a altura do triângulo em cm: '))

area = largura * altura / 2 

print(f'A área de um triângulo de altura {altura:.2f}cm e largura {largura:.2f}cm é igual a {area:.2f}cm')