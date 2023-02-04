#  Programa Principal
palavra = input("Digite uma palavra: ")

for letra in palavra:
    print (palavra)
    palavra = palavra[1:] + palavra[0] # palavra = palavra [1:] + letra

print(palavra)