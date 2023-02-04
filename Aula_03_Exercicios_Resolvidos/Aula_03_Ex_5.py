# Programa Principal

x = float(input("Digite o valor de x: "))

y = float(input("Digite o valor de y: "))

aux = x
x = y
y = aux

print("Os novos valores de x e y são, respectivamente: %.2f e %.2f" %(x,y))