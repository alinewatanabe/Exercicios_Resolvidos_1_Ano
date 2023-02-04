# Importação dos módulos
from math import log10, trunc

# Definição das funções
def exibeFração(n,d):
    """exibe a fração na forma bonitinha"""
    nDigN = trunc(log10(n)) + 1
    nDigD = trunc(log10(d)) + 1
    nDig = max(nDigN, nDigD)
    print("%s%i" %(" "*(nDig - nDigN), n))
    print("-"*nDig)
    print("%s%i" %(" "*(nDig - nDigD), d))

# Programa Principal
n1 = int(input("Digite o numerador da fração 1: "))
d1 = int(input("Digite o denominador da fração 1: "))

exibeFração(n1, d1)

n2 = int(input("Digite o numerador da fração 2: "))
d2 = int(input("Digite o denominador da fração 2: "))

exibeFração(n2, d2)

n = n1*d2 + n2*d1
d = d1*d2

print(" A soma das duas frações é: ")
exibeFração(n,d)