# Programa Principal
Frase = input("Digite a frase: ")
palavra = input("Digite a palavra: ")

frase = Frase.lower()
N = frase.count(palavra)

print("A palavra '%s' aparece '%i' vezes na frase '%s' " %(palavra, N, Frase))