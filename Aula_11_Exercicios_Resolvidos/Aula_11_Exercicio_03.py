# Programa Principal
Frase = input("Digite a frase: ")
c = input("Digite o caractere: ")

frase = Frase.lower()
n = frase.count(c)

print("Aparece %i vezes o caractere '%s' na frase '%s'" %(n,c,Frase))
