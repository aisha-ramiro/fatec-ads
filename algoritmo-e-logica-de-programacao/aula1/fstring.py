# -*- coding: utf-8 -*-

# 9. F-Strings

aluno = input('Digite o nome do aluno: ')
nota = float(input('Digite o valor da nota: '))

print(f'A nota do(a) aluno(a) {aluno} é: {nota:.1f}') 
# o f-strings é uma forma mais simples de formatar e concatenar as strings. 
#É necessário utilizar o prefixo f e declarar as variáveis dentro de {}.

# Obs. Utilizei o float(input()) para inserir o valor da nota.
# na segunda variável, usei o .1f para formatar o valor de nota e mostrar 
# uma casa decimal.