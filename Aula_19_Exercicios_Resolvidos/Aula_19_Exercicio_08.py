# Definição das Funções
def ExibeNotas(D):
    """Exibe a tabela com as notas"""
    alunos = list(D.keys())
    alunos.sort()
    print("%15s\t%4s\t%4s\t%4s\t%4s" %("RA","P1","P2","P3","P4"))
    for a in alunos:
        print("%15s\t%4s\t%4s\t%4s\t%4s" %(a,D[a][1],D[a][2],D[a][3],D[a][4]))

# Programa Principal
dados = "16.96125-7\t8.5,4.5,7,6\n15.07896-3\t4,5,6,7\n16.06542-3\t7,8.5,7,7.5"
D = {}
alunos = dados.split("\n")

for aluno in alunos:
    linha = aluno.slipt("/t")
    RA = linha[0]
    notas = linha[1].split(",")
    print(RA,notas)
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    D[RA] = notas

ExibeNotas(D)
op = "S"
while (op == "S"): 
    RA = input("Digite o RA que deseja calcular a média: ")

    if RA in D:
        media  = sum(D[RA])/len(D[RA])
        print("A média é: %1.f" %media)
    else:
        print("RA não cadastrado!")
    op = input("Deseja calular a média de outro RA? [S/N]\n ").upper()