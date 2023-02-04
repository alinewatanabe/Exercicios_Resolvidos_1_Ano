# Definição das funções
def exibeTabela(Tabela):
    """exibe a tabela formatada"""
    print("%15s\t%15s" % ("Categoria", "Produto"))
    for linha in Tabela:
        print("%15s\t%15s" % tuple(linha))


# Programa principal
N = int(input("Digite o número de itens: "))
Tabela = []
for i in range(N):
    produto = input("Digite o produto %i: " %(i+1)).lower()
    categ = input("Digite a categoria do '%s': " %produto).lower()
    Tabela.append( [categ, produto] )
    
Tabela.sort()
    
exibeTabela(Tabela)
