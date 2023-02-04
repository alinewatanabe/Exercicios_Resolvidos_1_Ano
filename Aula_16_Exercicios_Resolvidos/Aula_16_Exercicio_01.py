# Definição das funções
def exibeTabela(Tabela):
    """exibe a tabela formatada"""
    print("%15s\t%15s" % ("Temperatura", "Viscosidade"))
    for linha in Tabela:
        print("%15.2f\t%15.2f" % tuple(linha))

def retornaMaior(Tabela):
    """retorna o indíce da maior viscosidade"""
    y = Tabela[0][1]
    Lin = 0
    for L in range(len(Tabela)):
        linha = Tabela[L]
        if linha[1] > y:
            y = linha[1]
            Lin = L
    return Lin

# Programa principal
N = int(input("Digite o número de itens: "))
Tabela = []
for i in range(N):
    temp = float(input("Digite a temperatura %i: " %(i+1)))
    visc = float(input("Digite a viscosidade %i: " %(i+1)))
    Tabela.append( [temp, visc] )
    
exibeTabela(Tabela)
i = retornaMaior(Tabela)

print("A temperatura na qual a viscosidade é máxima é: %.2f" %Tabela[i][0])
