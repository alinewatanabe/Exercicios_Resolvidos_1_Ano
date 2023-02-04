# Programa Principal
frase = input("Digite uma frase: ").replace(" ","")

d = {}

for c in frase:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(d)

