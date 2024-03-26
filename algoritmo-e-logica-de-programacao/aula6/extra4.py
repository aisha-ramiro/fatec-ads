# Leia o peso e a altura
# calcule o IMC
# mostre a faixa de peso baseada no IMC

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura**2)

if imc < 17:
    print(f'O seu IMC é de {imc:.2f}, está MUITO abaixo do peso!')
elif imc >= 17 and imc <= 18.49:
    print(f'O seu IMC é de {imc:.2f}, está abaixo do peso!')
elif imc >= 18.5 and imc <= 24.99:
     print(f'O seu IMC é de {imc:.2f}, está com o peso ideal!')
elif imc >= 25 and imc <= 29.99:
     print(f'O seu IMC é de {imc:.2f}, está acima do peso!')
elif imc >= 30 and imc <= 34.99:
     print(f'O seu IMC é de {imc:.2f}, está com obesidade I !')
elif imc >= 35 and imc <= 39.99:
     print(f'O seu IMC é de {imc:.2f}, está com obesidade II !')
else:
     print(f'O seu IMC é de {imc:.2f}, está com obesidade MÓRBIDA!')