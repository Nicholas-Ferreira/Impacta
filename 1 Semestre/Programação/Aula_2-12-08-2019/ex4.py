temp = [27.5, 40, 12, 0.1, 20, 2, 5, 9, 25, 5.36, 18, 20]

media = sum(temp) / 12 
print(media)

acima = [i for i in temp if i > media]
print(acima)

