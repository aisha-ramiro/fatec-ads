#Exercicio 7

custo_fabrica = float(input('Digite o custo de fábrica do carro: R$ '))

distribuidor = custo_fabrica * (28/100)
impostos = custo_fabrica * (45/100)

custo_consumidor = custo_fabrica + distribuidor + impostos

print(f'''
  Custo de fábrica: R$ {custo_fabrica:.2f}
  Custo de distribuição: R$ {distribuidor:.2f}
  Custo dos impostos: R$ {impostos:.2f}

  Custo do consumidor: R$ {custo_consumidor:.2f}
''')

