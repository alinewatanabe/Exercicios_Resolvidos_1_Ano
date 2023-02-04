# Definição das funções
def procuravalor(d,n):
    """Retorna uma lista ordenada com as chaves que possuem o valor n"""
    L = []
    for item in d:
        if (n in d[item]):
            L.append(item)
    L.sort()
    return L

# Programa Principal
d = {}
l = []
C = "S"
while (C == "S"):
    
    chave = input("Digite a chave dicionário: ").lower()
    N = 1
    l = []
    while (N <= 3):
        valor = int(input("Digite o %i° valor: " %N))
        N += 1
        l.append(valor)
        d[chave] = l
    C = input("Deseja adicionar mais uma chave? [S/N]\n").upper()
print(d)
n = int(input("Digite o valor de n: "))
print(procuravalor(d, n))  
