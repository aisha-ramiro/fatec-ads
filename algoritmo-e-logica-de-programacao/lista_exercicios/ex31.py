def calcular_e(n):
    e = 1  
    fatorial = 1  

    for i in range(1, n + 1):
        fatorial *= i  
        e += 1 / fatorial  

    return e

e_3_termos = calcular_e(3)
print("E com 3 termos:", e_3_termos)

e_4_termos = calcular_e(4)
print("E com 4 termos:", e_4_termos)

e_5_termos = calcular_e(5)
print("E com 5 termos:", e_5_termos)
