# Programa Principal
N = int(input("Digite a quantidade de valores: "))
i = 0
Soma = 0
while (i < N):
    X = float(input("Digite um valor: "))
    Soma += X**2
    i += 1

print("A Soma dos quadrados desses valores é: %.2f "%Soma)