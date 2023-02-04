# Programa Principal
Frase = input("Digite uma frase: ")
Letra = input("Digite uma palavra: ")

frase = Frase.title()
letra = Letra.upper()

c = frase.count(letra)
    
print("A frase '%s' apresenta %i palavras que começam com a letra '%s'." %(Frase, c, Letra))