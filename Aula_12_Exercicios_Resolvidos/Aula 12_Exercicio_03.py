# Programa principal
frase = input("Digite uma frase: ").lower()

maiorPalavra = ""
aux = ""

for letra in frase:
    if letra not in ' ,.;:!?':
        aux = aux + letra
    else:
        if len(aux) > len(maiorPalavra):
            maiorPalavra = aux
        aux = ""
# última palavra
if len(aux) > len(maiorPalavra):
    maiorPalavra = aux    
    
print("A maior palavra da frase é '%s' com %i caracteres" % (maiorPalavra, len(maiorPalavra)))
