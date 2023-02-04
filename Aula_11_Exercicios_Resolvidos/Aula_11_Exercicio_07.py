# Definição das Funções
def trasprafrente(frase):
    """Essa função faz com que a frase original passe a ser escrita de tras pra frente"""
    resp = ''
    for c in frase:
        resp = c + resp
    return resp

# Programa Principal
frase = input("Digite uma frase: ")

ftpf = trasprafrente(frase)

print('A frase "%s" passa a ser "%s"' %(frase,ftpf))