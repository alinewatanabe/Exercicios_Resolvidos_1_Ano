# Programa principal
n = -1
while n <= 0:
    n = int(input("Digite o valor de n: "))
    if n <= 0:
        print("Digite um valor maior que 0.")
        
i = 2
aux = 0
while i <= n-1:
    if n%i == 0:
        print(n, "é divisível por", i)
        aux += 1
    i += 1
        
if aux == 0:
    print(n, "é primo.")
else:
    print(n, "não é primo.")
