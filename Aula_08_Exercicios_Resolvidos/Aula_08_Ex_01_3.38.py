# Importação dos módulos
from math import pi

# Programa principal
D = float(input("Digite o valor de D: "))
Q = float(input("Digite o valor de Q: "))

if D > 100:
    n = 2
elif D < 50:
    n = 6
else:
    n = 4
    
S = (4*Q*n)/(pi*D**2)
print("S = %.2f" %S)
