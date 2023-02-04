# Programa Principal
tarefas = {}
dias = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]
op = "S"
while (op == "S"):
    nome = input("Digite o nome de quem vai fazer a tarefa: ").title()
    dia = input("Digite o dia que a tarefa vai ser realizada: ").title()
    tarefa = input("Digite a tarefa a ser realizada: ").lower()
    if nome not in tarefas:
        tarefas[nome] = {dia: tarefa}
    else:
        if dia not in tarefas[nome]:
            tarefa[nome][dia] = tarefas
        else:
            print("%s já possui tarefa neste dia." %nome)
    
    
    op = input("Digite inserir outra tarefa [S/N]?\n").upper()

for d in dias:
    print(d)
    for p in tarefas:
        if d in tarefas[p]:
            print("%s deve %s" %(p,tarefas[p][d]))
    print()