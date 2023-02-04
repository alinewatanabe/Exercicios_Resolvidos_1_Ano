#  =Importação de Módulo
import numpy as np

# Programa Principal
L = []
ordem = int(input("Digite a ordem do polinomio: "))
n = ordem + 1

while (n > 0):
    coef = float(input("Digite os coeficientes"))
    L.append(coef)
    n -= 1

P = np.poly1d(L)
r = P.r
i = np.imag(P)

print(r)
print(i)
