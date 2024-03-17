# AREA RETANGULO E CIRCULO

print('''
  Esolha uma das opções para calcular a área:
    1. Retângulo
    2. Círculo
''')
  
opcao = input('Digite o número da opção desejada: ') 

#vai armazenar a escolha do usuário para redirecionar para o cálculo

if opcao == '1': #calcula a área do retangulo caso o usuário escolha
  print('Vamos calcular a área de um retângulo!')
  largura = float(input('Digite a largura em cm: '))
  altura = float(input('Digite a altura em cm: '))
  area = largura * altura
  print(f'A área do retângulo de largura {largura:.2f}cm e altura {altura:.2f}cm é de {area:.2f}cm')

elif opcao == '2': #calcula a área do círculo caso o usuário escolha
  print('Vamos calcular a área de um círculo!')
  raio = float(input('Digite o raio do círculo em cm: '))
  area = 3.14159 * (raio ** 2)
  print(f'A área do circulo de raio {raio:.2f}cm é de {area:.2f}cm')

else: #gera um erro caso o usuário não escolha uma opção válida
  print("Opção inválida, por favor, digite '1' para retângulo e '2' para círculo!")