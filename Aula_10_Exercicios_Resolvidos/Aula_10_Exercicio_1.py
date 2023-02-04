# Importação dos módulos
from math import sqrt

# Programa principal
L = float(input("Digite o tamanho inicial L: "))
N = int(input("Digite a quantidade de elementos: "))

A0 = (L**2)*sqrt(3)/4

S = 0 #acumulador
k = 1 #contador

while k <= N:
    S += (4/9)**(k-1) #S = S + (4/9)**(k-1)
    k += 1 #k = k + 1
    
AFN = (1+S/3)*A0
print("A área do floco de neve é: %.2f" %AFN)
