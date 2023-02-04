# Programa Principal
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
    if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
        print("O triângulo é retângulo.")
        if (a > b > c) or (a > c > b):
            print ("%.2f é a hipotenusa e %.2f e %.2f são catetos" %(a,b,c))
        elif (b > a > c) or (b > c > a):
            print ("%.2f é a hipotenusa e %.2f e %.2f são catetos" %(b,a,c))
        else:
            print ("%.2f é a hipotenusa e %.2f e %.2f são catetos" %(c,b,a))        
    else:
        print("Não é um triângulo retângulo")
else:
    print("Não é triângulo.")