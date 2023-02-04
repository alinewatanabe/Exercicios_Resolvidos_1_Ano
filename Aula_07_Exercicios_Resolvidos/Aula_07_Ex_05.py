# Definição das funções
def bissexto(ano):
    """retorna se o ano é bissexto ou não"""
    return (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))

# Programa principal
ano = int(input("Digite o ano: "))

if bissexto(ano):
    print("O ano de %i é bissexto." %ano)
else:
    print("O ano de %i não é bissexto." %ano)
