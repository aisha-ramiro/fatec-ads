#faça um programa que leia do usuário um número e calculo o produtório de 1 até esse número

n = int(input('Digite um número: '))

produto = 1
for num in range(1, n+1):
    produto *= num
    
print(f"O produtório dos números de 1 a N é: {produto}")
