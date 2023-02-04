# Importação dos módulos 

import matplotlib.pyplot as plt 

import numpy as np 

  

# Programa principal 

gastos = {"casa": 0, "alimentação": 0, "saúde": 0, "transporte": 0, "educação": 0, "lazer": 0, "outros": 0} 

  

tipo = input("Digite a categoria do gasto ou vazio para sair: ").lower() 

while tipo != "": 

    valor = float(input("Digite o valor do gasto: ")) 

    if tipo in gastos: 

        gastos[tipo] += valor 

    else: 

        gastos["outros"] += valor 

    tipo = input("Digite a categoria do gasto ou vazio para sair: ").lower() 

  

categ = gastos.keys() 

valores = gastos.values() 

  

iBarra = np.arange(len(valores))  # 0, 1, 2, 3, 4, 5 

larg = 0.9 # 100% da largura da barra 

  

plt.ylabel('Gastos Mensais') 

plt.xticks(iBarra, categ) 

  

plt.bar(iBarra, valores, width=larg) 

plt.show() 

 