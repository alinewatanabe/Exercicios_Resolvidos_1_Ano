# Programa Principal
N = int(input("Digite a quantidade de termos: "))
d = float(input("Digite o valor a ser somado: "))
p = 0
while (N < 0):
    print("A quantidade precisa ser maior ou igual a zero")
    N = int(input("Digite a quantidade de termos: "))

if (N > 0):
    sinal = -1
    i = 1
    while (N > 0):
        p += sinal*1/(i+d)
        i += 1
        sinal *= -1
        N -= 1

else:
    p = -99
    
print("A somatória será igual a %.2f" %p)