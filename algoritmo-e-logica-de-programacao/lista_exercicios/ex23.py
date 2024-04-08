def calcular_area_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
    else:
        return None

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

area_triangulo = calcular_area_triangulo(a, b, c)
if area_triangulo is not None:
    print("Os valores formam um triângulo e a área é:", area_triangulo)
else:
    print("Os valores fornecidos não formam um triângulo.")
