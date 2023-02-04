# Programa principal
p1 = input("Digite uma palavra: ").lower()
p2 = input("Digite uma palavra: ").lower()
p3 = input("Digite uma palavra: ").lower()

if p1 <= p2 <= p3:
    print (p1, p2, p3)
elif p1 <= p3 <= p2:
    print (p1, p3, p2)
elif p2 <= p1 <= p3:
    print (p2, p1, p3)
elif p2 <= p3 <= p1:
    print (p2, p3, p1)
elif p3 <= p1 <= p2:
    print (p3, p1, p2)
elif p3 <= p2 <= p1:
    print (p3, p2, p1)
