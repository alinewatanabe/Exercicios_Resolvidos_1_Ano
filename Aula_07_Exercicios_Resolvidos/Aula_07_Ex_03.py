# Importação de Módulo

# Programa Principal
a = int(input("Digite o lado 'a': "))
b = int(input("Digite o lado 'b': "))
c = int(input("Digite o lado 'c': "))

if (a<b+c) and (b<a+c) and (c<a+b):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print("A área do triângulo é: %.2f" %area)
else:
    print("Os lados não formam um triângulo.")
