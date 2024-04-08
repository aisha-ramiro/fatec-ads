#Exercicio 14

codigo = input('Digite o código do aluno: ')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

maior_nota = max(nota1, nota2, nota3)

if maior_nota == nota1:
  media = (nota1 * 4 + nota2 * 3 + nota3 * 3) / 10
elif maior_nota == nota2:
  media = (nota1 * 3 + nota2 * 4 + nota3 * 3) / 10
else:
  media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10


if media >= 5: 
  situacao = 'APROVADO'
else:
  situacao = 'REPROVADO'

print(f'''
  Código do aluno: {codigo}

  Nota 1: {nota1:.2f}
  Nota 2: {nota2:.2f}
  Nota 3: {nota3:.2f}
  Média final: {media:.2f}

  Situação: {situacao}
''')