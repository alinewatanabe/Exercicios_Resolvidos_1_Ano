# Programa Principal
A = float(input("Digite o valor de A [A > 0]: "))
B = float(input("Digite o valor de B [B >= A]: "))
N = float(input("Digite a quantidade de número que deseja encontrar [N > 0]: "))
C = 0
i = 1

while (A <= 0):
    print("O valor de A precisa ser um número positivo")
    A = float(input("Digite o valor A: "))

while (B < A):
    print("O valor de B precisa ser maior ou igual ao valor de A.")
    A = float(input("Digite o valor de A [A > 0]: "))
    B = float(input("Digite o valor de B [B >= A]: "))

while (N < 0):
    print("A quantidade precisa ser maior que zero")
    N = float(input("Digite o valor de N [N > 0]: "))


while (i <= N):
    C = A*i
    i += 1
    print(C)
