# Programa principal
N = int(input("Digite um n�mero com 4 algarismos: "))

A = N // 100
B = N % 100
if (A+B)**2 == N:
    print("%i possui a propriedade." %N)
else:
    print("%i não possui a propriedade." %N)

