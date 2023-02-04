# Importação dos Módulos
from os import system

# Definição das Funções
def ExibeQuadro(D):
    """Exibe o quadro de medalhas"""
    system("cls")
    paises = list(D.keys())
    paises.sort()
    print("%25s\t%10s\t%10s\t%10s" %("País","Ouro","Prata","Bronze"))
    for p in paises:
        print("%25s\t%10s\t%10s\t%10s" %(p,D[p]["ouro"],D[p]["prata"],D[p]["bronze"]))
        
# Programa Principal
quadro = {}
pais = input("Digite o nome do país: ").title()
while pais != "":
    medalha = input("Digite a medalha conquistada [ouro,prata,bronze]: ").lower()
    if pais not in quadro:
        quadro[pais] = {"ouro":0,"prata":0,"bronze":0}
    quadro[pais][medalha] += 1
    ExibeQuadro(quadro)
    pais = input("Digite o nome do país: ").title()

ExibeQuadro(quadro)