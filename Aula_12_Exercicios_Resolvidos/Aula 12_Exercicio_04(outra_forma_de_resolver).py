# Definição das funções
def verificaAnagrama(p1, p2):
    """retorna se duas palavras são anagramas ou não"""
    if len(p1) == len(p2):
        aux = 0
        for letra in p1:
            if p1.count(letra) != p2.count(letra):
                aux += 1
        if aux == 0:
            return True
        else:
            return False
    else:
        return False

# Programa principal
p1 = input("Digite a primeira palavra: ").lower()
p2 = input("Digite a segunda palavra: ").lower()

if verificaAnagrama(p1, p2):
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")
