# Programa Principal

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

s = (a + b + c)/2

K = (s*(s-a)*(s-b)*(s-c))**1/2

print("O valor da área é: %.f" %K)