'''
Faça um programa que leia do usuário:
- Nota 1
- Nota 2 

Calcule a média = nota1 * 0.5 + nota 2 * 0.5
'''

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1*0.5) + (nota2*0.5)

print(f'A média final do aluno é de {media:.1f}')
