# Definição das funções
def delta(a, b, c):
    """retorna o valor de delta"""
    return b**2 - 4*a*c

# Programa principal
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

d = delta(a, b, c)
if d == 0:
    x = -b/(2*a)
    print("Duas raízes reais iguais:")
    print("x1 =", x)
    print("x2 =", x)
elif d > 0:
    x1 = (-b -d**(1/2))/(2*a)
    x2 = (-b +d**(1/2))/(2*a)
    print("Duas raízes reais distintas:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    x1 = (-b -d**(1/2))/(2*a)
    x2 = (-b +d**(1/2))/(2*a)
    print("Duas raízes complexas conjugadas:")
    print("x1 =", x1)
    print("x2 =", x2)
