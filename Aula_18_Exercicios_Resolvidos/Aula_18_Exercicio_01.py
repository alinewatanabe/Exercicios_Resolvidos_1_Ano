# Programa Principal
d = {}

a = "S"
while(a == "S"):
    codigo = input("Digite o código do novo projeto: ") # chave
    d[codigo] = int(input("Digite o tempo de execução do projeto: ")) # valor
    a = input("Deseja acrescentar mais um projeto?\t[S/N]\n").upper()

projetos = list(d.keys())
projetos.sort()

print("%10s\t%10s" %("Projeto","Tempo"))
for proj in projetos:
    print("%10s\t%10i" %(proj,d[proj]))
