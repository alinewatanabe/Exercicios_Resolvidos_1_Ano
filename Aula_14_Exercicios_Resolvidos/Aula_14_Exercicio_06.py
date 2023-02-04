# Definição das funções
def LerValores(L, N):
    for i in range(N):
        x = float(input("Digite um valor: "))
        L.append(x)

def LerValores1(L, N):
    for i in range(N):
        x = float(input("Digite o valor do peso: "))
        L.append(x)  
        
# Programa Principal
L = []
N = int(input("Digite a quantidade de valores que serão considerados na média: "))

LerValores(L, N)
a = sum(L)

print("ATENÇÃO! Agora você deve colocar os valores dos pesos")
L1 = []
LerValores1(L1,N)
b = a*L[0]
c = sum(L1)

Media = b/c
print(Media)