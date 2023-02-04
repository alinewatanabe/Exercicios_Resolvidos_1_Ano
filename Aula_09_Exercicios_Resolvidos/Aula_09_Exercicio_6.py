# Programa Principal
a = float(input("Digite o valor de a: "))
x = a

while ((abs(x**3-a)) > 10**-6):
    xn = x - (((x**3) - a)/(3*(x**2)))
    x = xn

print("A raiz cúbica de %.2f é %.2f" %(a,x))