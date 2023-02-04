# Programa Principal
s = input().split(r"\n")
L = []
Lista_notas = []
Lista_nomes = []
Lista_medias = []
e = 0
for  c in s:
    L.append(c.split(r"\t"))
for a in L:
    Lista_notas.append(a[1].split(","))
    Lista_nomes.append(a[0])
for b in Lista_notas:
    for d in b:
        e += float(d)
    M = e/4
    e = 0
    Lista_medias.append(M)
print("%15s\t%15s" %("Nomes", "Médias"))

for n in range(len(Lista_nomes)):
    print("%15s\t%15.2f"%(Lista_nomes[n],Lista_medias[n]))
    