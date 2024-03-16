# SOMA DE DOIS NÚMEROS
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

soma = num1 + num2

print(f'A soma dos números {num1:.2f} e {num2:.2f} é igual a {soma:.2f}')

#Obs: soma simples de dois numeros digitados pelo usuário


# MÉDIA DE TRÊS NOTAS
total_notas = int(input('Digite o número de notas a serem consideradas: '))

notas = []
for i in range(total_notas):
  while True:
    nota = float(input(f'Digite a {i+1}ª nota: '))
    if 0 <= nota <= 10:
      notas.append(nota)
      break
    else:
      print(f"A nota {nota} fornecida é invalida, por favor, insira uma nota entre 0 e 10.")

media_notas = sum(notas) / len(notas)

print(f'A média final do aluno foi de {media_notas:.2f}')

#Obs: Entrada do usuário de quantas notas serão usadas na operação
# usando o total_notas, faço um loop de acordo com o número inserido
# alocando os valores em um único array.
# A partir disso, somo os valores do array e os divido pelo número de 
#elementos que compoem o array, gerando a média