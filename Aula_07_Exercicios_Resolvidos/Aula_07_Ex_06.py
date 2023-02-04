# Programa Principal

latas = 18*6
galoes = 3.6*6
quartos = 0.9*6

n_lat = 0
n_gal = 0
n_qua = 0

p_lata = 209.9
p_quarto = 30.9
p_galao = 78.9

area = float(input("Digite a area a ser pintada em m²: "))

area_ref = area*1.1

while area_ref >= latas:
    area_ref -= latas
    n_lat += 1

while area_ref >= galoes:
    area_ref -= galoes
    n_gal += 1

while area_ref >= quartos:
    area_ref -= quartos
    n_qua += 1

if (area_ref < quartos) and (area_ref > 0):
    n_qua += 1
    

preco_total = (n_lat*p_lata) + (n_gal*p_galao) + (n_qua*p_quarto)

print("Quantidade de latas: %i\nQuantidade de galoes: %i\nQuantidade de quartos: %i\nPreço Total: %.2f" %(n_lat, n_gal, n_qua,preco_total))