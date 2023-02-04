# Definição das funções
def LerLista(L, N):
    for i in range(N):
        x = float(input("Digite um valor: "))
        L.append(x)

# Programa principal
N = int(input("Digite o número de itens: "))
Lista = []
LerLista(Lista, N)
print(Lista)

Ndesl = int(input("Digite o número de vezes que será deslocada a lista: "))
desl = input("A lista será deslocada para esquerda ou direita? [d/e]  ").lower()

if desl == "d":
   for i in range(Ndesl):
       a = Lista.pop()
       Lista.insert(0,a)

else:
    for i in range(Ndesl):
        a = Lista.pop(0)
        Lista.append(a)

print(Lista)
   