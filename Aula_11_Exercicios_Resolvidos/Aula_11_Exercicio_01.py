#  Prrograma Principal
frase = input("Digite a frase: ")

Nt = len(frase)
Np = frase.count(" ") + 1

print(' A frase: "%s" contém %i caracteres e %i palavras' %(frase, Nt, Np))
