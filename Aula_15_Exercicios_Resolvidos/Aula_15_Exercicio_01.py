# Programa principal
frase = input("Digite uma frase: ").lower()
palavra = input("Digite uma palavra: ").lower()

L = frase.split()
a = L.count(palavra)

print('A palavra "%s" aparece %i vezes na frase.' %(palavra, a))
