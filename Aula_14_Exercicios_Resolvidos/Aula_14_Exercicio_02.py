# Importando bibliotecas
from math import sqrt

# Definção das funções
def LerValores (L,N):
    i = 0
    while i < N:
        x = float(input("Digite um valor: "))
        L.append(x)
        i = i + 1

# Programa Principal
N = int(input("Digite um o número de valores: "))
X = []
LerValores(X,N)

Media = sum(X)/N

S = 0
i = 0
while (i < N):
    S += (X[i] - Media)**2
    i += 1

DP = sqrt(S/(N - 1))

print("Os valores da média e do desvio padrão são respectivamente: %.2f e %.2f" %(Media, DP))