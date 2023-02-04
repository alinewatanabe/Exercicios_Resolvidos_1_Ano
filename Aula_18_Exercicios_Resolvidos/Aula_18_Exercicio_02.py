# Programa Principal
d = {}
N = int(input("Digite o número de disparos feitos: "))
for i in range(N):
    x = float(input("Digite o valor de x do %iº disparo: " %(i + 1)))
    y = float(input("Digite o valor de y do %iº disparo: " %(i + 1)))
    D = (x**2 + y**2)**1/2
    pontos = 10 - D//10
    coordenadas = (x,y)
    d[coordenadas] = pontos

ponto_max = max(d.values())

print("%10s\t%10s" %("Disparos","Pontos"))
for i in d:
    if d[i] == ponto_max:
        print("%10s\t%10i" %(i,d[i]))
