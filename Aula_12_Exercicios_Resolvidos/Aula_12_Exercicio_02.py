# Definição das funções
def contaVogais(frase):
    """retorna a quantidade de vogais da frase"""
    vogais = frase.count("a") + frase.count("e") + frase.count("i") + frase.count("o") + frase.count("u") 
    return vogais

# Programa principal
frase = input("Digite uma frase: ").lower()

print("A frase possui %i vogais." %contaVogais(frase))
