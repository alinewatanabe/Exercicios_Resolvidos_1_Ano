# Importação dos módulos
from math import tan, radians

# Deifnições das funções
def parcela(x,n):
    """retorna o valor de tan(x)88n/n"""
    x = radians(x)
    return (tan(x)**n)/n

# Programa Principal
a = float(input("Digite o valor do ângulo a [graus]: "))
b = float(input("Digite o valor do ângulo b [graus]: "))
c = float(input("Digite o valor do ângulo c [graus]: "))

d = 1 + parcela(a,2) + parcela(b,3) + parcela(c,4)

print("d= %.2f" %d)