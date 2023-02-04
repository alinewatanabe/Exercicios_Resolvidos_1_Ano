# Programa Principal
Frase = input("Digite uma frase: ")

frase = Frase.lower()
n = 0

for letra in frase:
    if frase.count(letra) > n:
        n = frase.count(letra)
        l = letra
print("O  caractere '%s' apareceu %i na frase '%s'" %(l,n, Frase))