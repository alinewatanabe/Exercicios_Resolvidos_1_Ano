# Programa Principal
L = []
while True:
    print("Digite N para adicionar um novo cliente.")
    print("Digite P para avisar que o pedido está pronto.")
    print("Digite S para sair.")
    a = input("Qual operação você deseja fazer? ").upper()
    if a == "N":
        b = input("Digite o nome do cliente: ").upper()
        L.append(b)
        
    elif a == "P":
        c = L.pop(0)
        print(c)
        
    elif a == "S":
        break
    
    else:
        print("Operação inválida. Digite apenas um dos tres comandos")