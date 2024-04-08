ipi = float(input("Digite a porcentagem do IPI a ser acrescido: "))

codigo_peca_1 = int(input("Digite o código da peça 1: "))
valor_unitario_peca_1 = float(input("Digite o valor unitário da peça 1: "))
quantidade_peca_1 = int(input("Digite a quantidade de peças 1: "))

codigo_peca_2 = int(input("Digite o código da peça 2: "))
valor_unitario_peca_2 = float(input("Digite o valor unitário da peça 2: "))
quantidade_peca_2 = int(input("Digite a quantidade de peças 2: "))

total = (valor_unitario_peca_1 * quantidade_peca_1 + valor_unitario_peca_2 * quantidade_peca_2) * (ipi / 100 + 1)

print("Valor total a ser pago:", total)
