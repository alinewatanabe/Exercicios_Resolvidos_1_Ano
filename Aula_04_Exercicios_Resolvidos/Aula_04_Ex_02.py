# Importação dos modulos
from math import exp

# Definição das funções
def cos_hip(x):
    """retornao valor de cosseno hiperbólico de x"""
    return (exp(x) + exp(-x))/2

# Programa Principal
x = float(input("Digite o valor de x: "))

c = cos_hip(x)

print("cosh(x) = %.4f" %c)
