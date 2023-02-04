# Definição das funções
def maiorMenor(Lista):
    """retorna o maior e o menor elemento da lista"""
    return (max(Lista), min(Lista))

# Programa principal
N = int(input("Digite o número de itens: "))
Lista = []
for i in range(N):
    x = float(input("Digite o valor de x%i: " %(i+1)))
    Lista.append(x)
    
print(maiorMenor(Lista))
