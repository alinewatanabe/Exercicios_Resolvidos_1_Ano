# Programa Principal
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a != b != c:
        print("É um triângulo escaleno.")
    else:
        print("É um triângulo isóceles.")
else:
    print("Não é um triângulo.")