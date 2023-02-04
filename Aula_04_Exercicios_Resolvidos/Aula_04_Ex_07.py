# Importação dos módulos
from math import radians, tan

# Definição das funções
def CalcularAltura(h,CA,ang):
    """retorna a altura maior de um trapézio"""
    ang = radians(ang)
    return CA*tan(ang) + h

def AreaTrapezio(B, b, h):
    """retorna a área de um trapézio"""
    return (B+b)*h/2
    
# Programa Principal
comp = float(input("Digite o comprimento: "))
larg = float(input("Digite a largura: "))
h0 = float(input("Digite a altura menor: "))
alfa = float(input("Digite alfa (em graus): "))
beta = float(input("Digite beta (em graus): "))

HL = CalcularAltura(h0, larg, beta)
HC = CalcularAltura(h0, comp, alfa)
HT = CalcularAltura(HC, larg, beta) 
# o HT pode ser calculado também como HT = CalcularAltura(HL, comp, alfa)

A1 = AreaTrapezio(HC, h0, comp)
A2 = AreaTrapezio(HL, h0, larg)
A3 = AreaTrapezio(HT, HL, comp)
A4 = AreaTrapezio(HT, HC, larg)

AT = A1 + A2 + A3 + A4
print("A área total do duto é %.2f m²" %AT)