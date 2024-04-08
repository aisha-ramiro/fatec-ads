# Exercicio 9

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
  print(f'A média do aluno é {media:.1f}, portanto está aprovado!')
else:
  print(f'A média do aluno é {media:.1f}, portanto está reprovado!')
