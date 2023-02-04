# Importação dos módulos
from math import sqrt, sin

# Definição das funções
def f(x):
    """retorna o valor de f(x)"""
    return sqrt(sin(x)**2 + 2*x)
    
# Programa principal
x0 = float(input("Digite o valor de x0: "))
h = 10**(-5)

m_sec = (f(x0 + h/2) - f(x0 - h/2))/h
print("O coeficiente angular da reta secante no ponto %.2f é %.4f" %(x0, m_sec))
