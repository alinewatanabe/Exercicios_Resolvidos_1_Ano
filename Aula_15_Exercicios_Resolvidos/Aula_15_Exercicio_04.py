# Importação dos módulos
from math import sin, radians

# Programa principal
comando = input("Digite o comando: ").lower()

# Retirar os espaços
comando = comando.replace(" ", "")

# Retirar o parênteses final
comando = comando.replace(")", "")

# Separar comando de parâmetros
comando = comando.split("(")

parametros = comando[1]
comando = comando[0]

# Separar os parâmetros
parametros = parametros.split(",")

# Transformar os parâmetros de string para float
for i in range(len(parametros)):
    parametros[i] = float(parametros[i])

# Calcular as respostas
if comando == "soma":
    resp = sum(parametros)
elif comando == "seno":
    resp = sin(radians(parametros[0]))
elif comando == "trapezio":
    resp = (parametros[0]+parametros[1])*parametros[2]/2
elif comando == "multiplica":
    resp = parametros[0]*parametros[1]
elif comando == "divide":
    if parametros[1] == 0:
        resp = "ERRO! Divisão por zero."
    else:
        resp = parametros[0]/parametros[1]
        
if type(resp) == float:
    print("resp = %.2f" %resp)
else:
    print(resp)

