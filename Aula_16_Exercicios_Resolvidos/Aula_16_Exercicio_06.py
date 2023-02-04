#  Definição das Funções
def ExibirTabela(Tabela):
    """exibe a tabela formatada"""
    Tabela.sort()
    Total = 0
    print("%20s\t%10s\t%10s" %("Produto","Quantidade","Preço"))
    for linha in Tabela:
        print("%20s\t%10.2f\t%10.2f" %tuple(linha))
        Total += linha[1]*linha[2]
    
    print("\nO custo total é: R$%.2f" %Total)
    
#  Programa Principal
print("Cadastro dos produtos\n\n")

N = int(input("Digite a quantidade de itens: "))

Tabela = []
for i in range(N):
    prod = input("Digite o produto %i: " %(i + 1)).lower()
    qtd= float(input("Digite a quantidade do produto %s") %(prod))
    Tabela.append([prod,qtd,0])

ExibirTabela(Tabela)

print("\n\nCadastro de Preços")

for i in range(N):
    prod = input("Digite o produto %i a ser cadastrado o preço: " %(i + 1)).lower()
    preço = float(input("Digite o preço do produto '%s'") %(prod))
    for linha in range(len(Tabela)):
        if Tabela[linha][0] == prod:
            Tabela[linha][2] = preço
        ExibirTabela(Tabela)
        
            