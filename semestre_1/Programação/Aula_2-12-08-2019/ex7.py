lista = [
    ['Brasil', 'Italia',  [10, 9]], 
    ['Brasil', 'Espanha', [5 , 7]], 
    ['Italia', 'Espanha', [7 , 8]]
]

total = 0
for jogo in lista:
    total += sum(jogo[2])

print(total)