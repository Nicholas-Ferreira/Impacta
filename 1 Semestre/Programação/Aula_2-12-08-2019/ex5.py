lista = [2.5, 7.5, 10.0, 4.0] 
media = sum(lista) / len(lista)

prox = [media-i for i in lista]

index = 0
for item in prox:
    if item < 0:
        prox[index] *= -1
    index += 1

print(min(prox)+media)