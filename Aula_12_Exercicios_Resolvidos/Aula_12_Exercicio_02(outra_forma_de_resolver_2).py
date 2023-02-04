# Definindo funções
def ContarVogais (frase):
    i = 0
    for letra in frase:
        if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
            i += 1
        print(letra)
            
# Programa Principal
frase = input("Digite uma frase: ").lower

a = ContarVogais(frase)
print(a)