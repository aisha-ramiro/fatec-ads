numero = int(input('Digite um número de 1 a 10: '))

def numeros_romanos(n):
    nums = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X'
    }

    if n in nums:
        return nums[n]
    else:
        return 'Digite apenas números de 1 a 10'

print(f'O número {numero} em algarismos romanos é: {numeros_romanos(numero)}')