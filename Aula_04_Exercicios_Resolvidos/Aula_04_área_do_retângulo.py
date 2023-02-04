# Definição das funções
def área_retângulo(base, altura):
    """retorna o valor da área de um retângulo dada a base e a altura"""
    return base*altura

# Programa Principal
b = float(input("Digite a base do retângulo em metros:"))
h = float(input("Digite a altura do retângulo em metros:"))

A = área_retângulo(b, h)
print("A área do retÂngulo é %.2f m²" %A)
help(área_retângulo)
