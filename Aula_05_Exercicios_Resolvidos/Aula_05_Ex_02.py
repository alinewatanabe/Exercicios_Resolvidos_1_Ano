# Definições das funções
def horario(a,b,c):
    """exibe a hora no formato sexagesimal"""
    print("%02ih:%02im:%02is" %(a,b,c))

# Programa Principal
h = float(input("Digite o valor das horas: "))
m = float(input("Digite o valor dos minutos:"))
s = float(input("Digite o valor dos segundos: "))

horario(h,m,s)