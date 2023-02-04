# Programa Principal

# Inserir as placas e as vagas
# Inserir uma placa e vaga nova
# Verificar se essa vaga esta livre
# Se a vaga estiver ocupada o programa deve pedir para tentar outra vaga
# Exibir uma tabela com todas as placas e suas respectivas placas
# A tabela deve estar ordenada pelo nº de vagas

placa_vaga = {}
vaga_placa = {}

a = "S"
while (a == "S"):
    placa = input("Digite a placa do carro: ").upper()
    placa_vaga[placa] = int(input("Digite a vaga do carro: ")) # vaga
    #valor_placa_vaga = placa_vaga.values()
    #valor_vaga_placa = vaga_placa.values()
    for i in vaga_placa:
        if valor_placa_vaga in vaga_placa:
            print("Está vaga já está ocupada. Tente outra vaga")
        else:
            placa_vaga[placa] = vaga_placa[placa]
    a = input("Deseja adicionar uma nova placa? [S/N]\n").upper()
    
print(placa_vaga,"placa_vaga")
print(vaga_placa,"vaga_placa")