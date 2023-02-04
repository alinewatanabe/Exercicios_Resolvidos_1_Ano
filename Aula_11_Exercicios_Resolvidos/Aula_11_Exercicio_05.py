# Definição das Funções
def teste(algo):
    resp = ''
    for c in algo:
        resp = c + resp
    return resp

# Programa Principal
a = input("Digite: ")

b = teste(a)

print(b)

"""Concluimos que a definição teste faz com que a frase digitada seja escrita de trás pra frente"""