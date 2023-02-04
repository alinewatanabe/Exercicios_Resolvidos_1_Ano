# Importação dos Módulos
import numpy as np
import matplotlib.pyplot as plt

# Programa Principal
x = np.linspace(-np.pi,np.pi,256, endpoint=True)
y = np.sin(x)/x

plt.title("Função sen(x)/x")
plt.plot(x,y)
plt.show()
