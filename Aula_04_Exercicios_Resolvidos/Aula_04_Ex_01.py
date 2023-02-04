# Importação dos módulos
from math import sin, radians

# Definições das funções
def Alcance(v0, teta):
    """retorna o alcance de um projétil dada a velocidade inicial v0 e o ângulo teta"""
    g = 9.81
    teta = radians(teta)
    return (v0**2/g)*sin(2*teta)

# Programa Principal
v0 = float(input("Digite a velocidade inicial [m/s]: "))
teta = float(input("Digite o ângulo de desparo [graus]: "))

S = Alcance(v0, teta)

print(" O alcance do porjétil é:%.2f m."%S)