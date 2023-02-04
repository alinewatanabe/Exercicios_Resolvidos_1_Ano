# Programa Principal
N = -1
while (N < 0):
    N = int(input("Digite o valor de N: [N>=0]: "))
    
i = N
fatorial = 1
while (i >= 1):
    fatorial = fatorial*i
    i = i - 1

print("O fatorial de %i é : %i" %(N,fatorial))