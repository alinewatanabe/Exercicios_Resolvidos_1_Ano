# Programa Principal
grau = int(input("Digite o grau do polinomio: "))

a = grau + 1
i = 0
L = []
while (i < a):
    b = float(input("Digite o coeficiente a%i: " %i))
    L.append(b)
    i += 1

x = float(input("Digite o valor de x: "))

s = "P(x) ="
e = 0
while (grau >= 0):
    e = e + (L[grau]*(x**(grau)))
    s += " %.1f*x**%i +" %(L[grau],grau)
    grau -= 1
print(s[:-1])    

print("P(%.1f) = %.1f" %(x,e))
