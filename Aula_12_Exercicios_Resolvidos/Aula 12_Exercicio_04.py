#  Programa Principal
palavra = input("Digite a 1ª palavra: ").lower()
palavra2 = input("Digite a 2ª palavra: ").lower()

if len(palavra) == len(palavra2):
    for letra1 in palavra:
       n1 = palavra.count(letra1)
       n2 = palavra2.count(letra1)
       if n1 == n2:
           n1 = 0
           n2 = 1
       else:
           n2 = 0
           print("Não é um anagrama.")
    if n2 == 1:
        print("Parabéns! Você tem um anagrama.")
    
else:
    print("Não é um anagrama.")