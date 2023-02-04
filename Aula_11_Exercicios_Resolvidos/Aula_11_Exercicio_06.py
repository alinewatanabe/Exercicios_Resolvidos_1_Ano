# Definição das Funções
def trasprafrente(frase):
    """Essa função faz com que a frase original passe a ser escrita de tras pra frente"""
    resp = ''
    for c in frase:
        resp = c + resp
    return resp
    
# Programa Principal
Frase = input("Digite uma frase: ")

frase = Frase.lower()
frase = frase.replace(" ","")
tpf = trasprafrente(frase)

if (frase == tpf):
    print ('A frase "%s" é um palíndromo' %Frase)

else:
    print ('A frase "%s" não é um palíndromo' %Frase)

