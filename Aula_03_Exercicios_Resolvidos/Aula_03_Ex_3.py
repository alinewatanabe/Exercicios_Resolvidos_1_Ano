# Programa Principal
valor = int(input("Digite o valor: "))
N50 = valor//50
R50 = valor%50
N10 = R50//10
N1 = R50%10

print("Para pagar a conta no valor de R$%.2f" %valor)
print("Valor vai precisar:")
print("%i notas de R$50.00" %N50)
print("%i notas de R$10.00" %N10)
print("%i moedas de R$1.00" %N1)
