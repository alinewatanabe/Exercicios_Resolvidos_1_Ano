# Programa principal
n = -1
while n < 0:
    n = int(input("Digite o valor de n: "))
    if n < 0:
        print("Digite um valor maior ou igual a 0.")
        
if n==0:
    p = -99
else:
    d = float(input("Digite o valor de d: "))
    i = 1 #contador
    p = 0 #acumulador    
    while i <= n:
        p += (-1)**i/(i+d)
        i += 1

print("p = %.2f" %p)
