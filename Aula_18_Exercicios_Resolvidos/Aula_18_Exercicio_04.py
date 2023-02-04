# Programa principal
frase = input("Digite a frase: ").replace(" ", "")
palavra = frase.slpit(" ")

d = {}
for p in palavra:
    if p in d:
        d[p] += 1
    else:
        d[p] = 1
        
print(d)
