# Importação dos módulos
from math import sqrt
# Definição das funções
def Lado(x1,x2,y1,y2):
    """ informa o x1,x2,y1,y2"""
    return  sqrt((x2 - x1)**2 - (y2 - y1)**2)

def calculaArea(a,b,c):
    """ retorna a área de um triângulo pela formula de Hierão"""
    p = (a + b + c)/2
    return sqrt(p*(p - a)*(p - b)*(p - c))

# Programa Principal
x1 = float(input("Digite o valor de x1: "))
x2 = float(input("Digite o valor de x2: "))
y1 = float(input("Digite o valor de y1: "))
y2 = float(input("Digite o valor de y2: "))
x3 = float(input("Digite o valor de x3: "))
y3 = float(input("Digite o valor de y3: "))

a = Lado(x1,x2,y1,y2)
b = Lado(x1,x3,y1,y3)
c = Lado (x2,x3,y2,y3)

área = calculaArea(a, b, c)

print("O valor do lado do triangulo é %.2f" %área)