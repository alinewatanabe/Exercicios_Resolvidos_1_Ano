# Programa Principal
d = {'ATC003':5,'ATC006':5,'ATC009':5,'ATC030':5,'ATC001':10,'ATC004':10,'ATC007':10,'ATC010':10,
     'ATC013':10,'ATC026':10,'ATC028':10,'ATC032':10,'ATC034':10,'ATC016':40,'ATC018':40,'ATC020':40,
     'ATC022':40,'ATC024':40,'ATC036':40}

a = 0
b = 0

N = int(input("Digite o número de atividade: "))
i = 0
while (i < N):
    atv = input("Digite o código da atividade: ").upper()
    if (atv in d):
        conceito = input("Digite o conceito recebido (C/N): ").upper()
        if (conceito == "C"):
            a += d[atv]
            b += d[atv]
            
        else:
            b += d[atv]
    else:
        print("Atividade não cadastrada")
    i += 1

print("Cumpriu %i de %i horas" %(a,b))
    