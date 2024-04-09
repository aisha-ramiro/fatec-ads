numero = int(input("Digite um número de 1 a 19: "))

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
        9: 'Nove',
        10: 'Dez',
        11: 'Onze',
        12: 'Doze',
        13: 'Treze',
        14: 'Quatorze',
        15: 'Quinze',
        16: 'Dezesseis',
        17: 'Dezessete',
        18: 'Dezoito',
        19: 'Dezenove'
    }

    if n in nums:
        return nums[n]
    else:
        return "Erro."


print(f"{numero}: {numeros_extenso(numero)}.")