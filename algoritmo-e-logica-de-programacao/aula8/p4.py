mes_u = input('Digite o mês: ')

def meses_ano (mes):
    meses = {
        'Janeiro': 31,
        'Fevereiro': 28,
        'Março': 31,
        'Abril': 30,
        'Maio': 31,
        'Junho': 30,
        'Julho': 31,
        'Agosto': 31,
        'Setembro': 30,
        'Outubro': 31,
        'Novembro': 30,
        'Dezembro': 31
    }

    if mes in meses:
        return meses[mes]
    else:
        return "Mês inválido."


print(f"O mês de {mes_u} tem {meses_ano(mes_u)} dias.")