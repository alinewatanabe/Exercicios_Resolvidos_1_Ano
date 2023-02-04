# 5.4 -> Construa um algoritmo em Python que leiam dois números inteiros a e b, um vetor inteiro
#        de tamanho n e exibam como resposta a contagem de quantos elementos do vetor estão no 
#        intervalo fechado [a,b]

# Programa Principal
a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))

N = int(input("Digite a quantidade de valores que deseja na lista: "))

i = 0
L = []
while (N > i):
    c = int(input("Digite um valor inteiro: "))
    L.append(c)
    i += 1

x = 0
for d in L:
    if (d <= b) and (d >= a):
        x += 1

print(x)