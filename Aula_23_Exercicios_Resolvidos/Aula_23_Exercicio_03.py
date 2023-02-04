# Importação de Módulos
import numpy as np

# Programa Principal
tabela = np.loadtxt('mapa.txt', delimiter = ";")
x1 = tabela[:,0]
y1 = tabela[:,1]
x = np.linspace(x1)