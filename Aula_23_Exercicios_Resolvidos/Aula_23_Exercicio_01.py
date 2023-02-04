# Importação de módulo
import matplotlib.pyplot as plt

# Programa principal
d = {"Alimentação":0, "Casa":0, "Saúde":0, "Transporte":0, "Educação":0, "Lazer":0, "Outros":0}

c = input("Digite a categoria: ").title()
v = float(input("Digite o valor: "))
z = "S"
while(z == "S"):
    if (c == "Alimentação" or "Casa" or "Saúde" or "Transporte" or "Educação" or "Lazer"):
        d[c] = v
    else:
        d["Outros"] = v
    z = input("Deseja continuar? [S/N]\n").upper()

y = d.keys()
l = d.values()
destacar = [0,0,0,0,0,0,0]
plt.title("Gastos")
plt.pie(l,labels=y,autopct="%.f%%", explode = destacar)
plt.axis("equal")
plt.tight_layout()

plt.show()