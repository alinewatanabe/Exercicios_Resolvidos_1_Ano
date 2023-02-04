#  Definindo as funções
def LerLista (L,N):
    i = 0
    while i < N:
        x = float(input("Digite um valor: "))
        L.append(x)
        i = i + 1
        
# Programa Principal
N = int(input("Digite o número de itens: "))
Lista = []
LerLista(Lista, N)

a = input("Você quer que a ordem seja crescente ou decrescente? [C/D] ").upper()

if a == "C":
    Lista.sort()

else:
    Lista.sort(reverse=True)

print(Lista)