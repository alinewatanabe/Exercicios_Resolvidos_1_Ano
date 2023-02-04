# Programa Principal
a = float(input("Digite o valor da altura [mm]: "))
h = float(input("Digite o valor do tempo [h]: "))
i = a/h

if i < 3:
    print("os valores estão considerados normais.")
elif (i >= 3) and (i < 8):
    print ("Os valores são considerados criticos.")

else:
    print("Os valores são considerados alarmantes.")    
