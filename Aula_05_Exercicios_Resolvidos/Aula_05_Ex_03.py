# Definição das funções
def exibeHora(d, h, m, s):
    """exibe a hora no formato sexagesimal"""
    h = h + 24*d
    print("%02ih%02im%02is" %(h, m, s))

# Programa principal
d = int(input("Digite os dias: "))
h = int(input("Digite as horas: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

exibeHora(d, h, m, s)
