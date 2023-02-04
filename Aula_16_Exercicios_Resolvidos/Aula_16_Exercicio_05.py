# Programa Principal
s = ["s2","p6","d10","f14"]
n = [1,2,3,4,5,6,7]

for linha in n:
    i = 1
    for coluna in s:
        a = "%i%s" %(linha,coluna)
        print("%4s"%a, end = "\t")
        if ((linha == 1) or (linha == 7)) and (i == 1):
            break
        if (linha == 2) and (i == 2):
            break
        if ((linha == 3) or (linha == 6)) and (i == 3):
            break
        i += 1        
    print()
        