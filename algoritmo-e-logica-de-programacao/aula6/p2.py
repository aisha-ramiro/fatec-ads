# Leia a nota e mostre: 
# nota >= 6:
# mostra('Aprovado')
# senão:
# mostra('Reprovado)

nota = float(input('Digite a nota do aluno: '))

if nota >= 6:
    print(f'O aluno tirou nota {nota:.2f} e está aprovado!')
else:
    print(f'O aluno tirou nota {nota:.2f} e está reprovado!')