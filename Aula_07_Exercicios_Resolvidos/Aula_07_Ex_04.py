# Programa Principal
d = float(input("Digite o valor da distancia a ser percorrida [km]: "))
if d <= 200:
    x = d*0.5
    print("O valor da passagem sera de R$%.2f."%x)
else:
    y = d*0.45
    print("O valor da passagem sera R$%.2f." %y)