# Definição das funções
def Bissexto(ano):
    """retorna se o ano é bissexto ou não"""
    return (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0))

# Programa principal
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes == 2:
    if Bissexto(ano):
        print("Esse mês tem 29 dias.")
    else:
        print("Esse mês tem 28 dias.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Esse mês tem 30 dias.")
else:
    print("Esse mês tem 31 dias.")
