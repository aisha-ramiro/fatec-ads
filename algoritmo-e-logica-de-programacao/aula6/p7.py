#Leia 2 números N1 e N2
# se N1 > N2:
#   mostrar('N1 é maior')
# senão
#   mostrar('N2 é maior)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O número {n1} é maior')
elif n1 == n2:
    print('Os números são iguais')
else:
    print(f'O número {n2} é maior')