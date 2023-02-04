# Programa principal
N = int(input("Digite um número com 4 algarismos: "))

A = N // 100
B = N % 100
if (A+B)**2 == N:
    print("%i possui a propriedade." %N)
else:
    print("%i nÃ£o possui a propriedade." %N)

