# Programa principal
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

# Versão if-else
if x == y:
    print("x é igual a y.")
else:
    if x > y:
        print("x é maior que y. x = %i" %x)
    else:
        print("y é maior que x. y = %i" %y)

# Versão elif
if x == y:
    print("x é igual a y.")
elif x > y:
    print("x é maior que y. x = %i" %x)
else:
    print("y é maior que x. y = %i" %y)
