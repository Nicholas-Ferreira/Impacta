notas = {}

def add_nota(nome, nota):
    if nome in notas:
        notas[nome] += [nota]
    else:
        notas[nome] = [nota]

def mediaaluno(nome):
    if nome in notas:
        return sum(notas[nome]) / len(notas[nome])

add_nota('Joao', 10)
add_nota('Joao', 10)

add_nota('Maria', 10)
add_nota('Maria', 10)

add_nota('Leo', 0)
add_nota('Leo', 2)

add_nota('Fernando', 6)
add_nota('Fernando', 7)

add_nota('Nicholas', 8) 
add_nota('Nicholas', 9)

print(notas)
print(mediaaluno('Joao'))

