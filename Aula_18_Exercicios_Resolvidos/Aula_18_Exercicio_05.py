# Programa Principal
d = {}
a = 'A'
b = 0
deposito = "Deposito"
saque = "Saque"
pagamento = "Pagamento"
d[deposito] = 0
d[saque] = 0
d[pagamento] = 0

print("Digite 'D' para realizar um deposito\nDigite 'S' para realizar um saque\nDigite 'P' para realizar um pagamento\nDigite 'F' para finalizar as transições")

while (a != 'F'):
    a = input("Qual operação deseja realizar?\n").upper()
    
    if (a == 'D'):
        b = float(input("Qual o valor da transição?\n"))
        d[deposito] += b

    if (a == 'S'):
        b = float(input("Qual o valor da transição?\n"))     
        d[saque] += b

    if (a == 'P'):
        b = float(input("Qual o valor da transição?\n"))
        d[pagamento] += b
    c = list(d.values())

e = c[0] - c[1] - c[2]

print("Fim das transações.\nVocê tem R$%.2f na conta." %e)
