# 5.3 -> Elabore um algoritmo em Python que calculem e exibam a diferença entre o maior e menor elemento de um vetor denominado VALORES (com N elementos). Tanto o número de elementos quanto o conteúdo do vetor denominado VALORES (com N elementos). Tanto o número de elementos quanto o conteúdo do vetor são valores lidos.

# Programa Principal
N = int(input("Digite a quantidade de valores: "))

i = 0
VALORES = []
while (i < N ):
    a = float(input("Digite um valor: "))
    VALORES.append(a)
    i += 1


b = max(VALORES)
c = min(VALORES)
d = b - c

e = len(VALORES)
print("Os valores digitados formam a lista:", VALORES)
print("Número de elementos:",e)
print("A diferença entre o maior e menor número:",d)
