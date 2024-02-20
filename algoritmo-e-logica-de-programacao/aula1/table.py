# -*- coding: utf-8 -*-

# 10. Tabela de Multiplicação

for n in range(1,6): 
  # loop externo para a linha, define o primeiro valor, n é a variável que 
  #será atribuida, 1 é onde começa e 6 onde termina, sendo o 6 excluído
  print(f'Tabuada do {n}')
  for i in range(1, 11): 
    # loop interno para a coluna, define o segundo valor, atribuido ao primeiro
    print(f'{n} x {i} = {n*i}')
  print('---')