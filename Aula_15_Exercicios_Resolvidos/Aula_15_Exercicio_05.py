# 6.3 -> Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos. Ao final exiba a lista em ordem crescente

# Definição das funções
def LerLista(L, N):
    for i in range(N):
        x = float(input("Digite um valor: "))
        L.append(x)

# Programa Principal
L = []
N = int(input("Digite quantos números a lista terá: "))
LerLista(L,N)

L2 = []
N2 = int(input("Digite quantos números a outra lista terá: "))
LerLista(L2,N2)

L3 = []

for elemento in L:
    L3.append(elemento)

for elemento in L2:
    if elemento not in L3:
        L3.append(elemento)

L3.sort()
print(L3)