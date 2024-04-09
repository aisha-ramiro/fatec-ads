numero = int(input("Digite um número de 1 a 9: "))

def numeros_extenso (n):
    nums = {
        1: 'Um',
        2: 'Dois',
        3: 'Três',
        4: 'Quatro',
        5: 'Cinco',
        6: 'Seis',
        7: 'Sete',
        8: 'Oito',
        9: 'Nove'
    }

    if n in nums:
        return nums[n]
    else:
        return "Erro."


print(f"{numero}: {numeros_extenso(numero)}.")