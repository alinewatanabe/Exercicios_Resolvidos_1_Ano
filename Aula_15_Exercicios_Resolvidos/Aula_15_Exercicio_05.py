# 6.3 -> Fa�a um programa que percorra duas listas e gere uma terceira sem elementos repetidos. Ao final exiba a lista em ordem crescente

# Defini��o das fun��es
def LerLista(L, N):
    for i in range(N):
        x = float(input("Digite um valor: "))
        L.append(x)

# Programa Principal
L = []
N = int(input("Digite quantos n�meros a lista ter�: "))
LerLista(L,N)

L2 = []
N2 = int(input("Digite quantos n�meros a outra lista ter�: "))
LerLista(L2,N2)

L3 = []

for elemento in L:
    L3.append(elemento)

for elemento in L2:
    if elemento not in L3:
        L3.append(elemento)

L3.sort()
print(L3)