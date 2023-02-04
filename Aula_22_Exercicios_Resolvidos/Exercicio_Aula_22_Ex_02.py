# Importação dos módulos 

import numpy as np 

import matplotlib.pyplot as plt 

  

# Definição das funções 

def R2(x,y,P): 

    SQres = sum((y - P(x))**2) 

    SQtot = sum((y - np.average(y))**2) 

    return 1 - SQres/SQtot 

  

# Programa principal 

qtd = int(input("Digite a quantidade de pontos: ")) 

  

x = [] 

y = [] 

  

for i in range(qtd): 

    x_val = float(input("Digite a coordenada x%i: " %i)) 

    y_val = float(input("Digite a coordenada y%i: " %i)) 

    x.append(x_val) 

    y.append(y_val) 

  

ordem = int(input("Digite a ordem do polinômio de ajuste: ")) 

P = np.poly1d( np.polyfit(x, y, ordem ) ) 

  

print(P) 

print("R² = %.4f" % R2(x,y,P)) 

  

x_graf = np.linspace(min(x), max(x)) 

y_graf = P(x_graf) 

plt.plot(x, y, "ro") 

plt.plot(x_graf, y_graf, "b--") 

plt.show() 