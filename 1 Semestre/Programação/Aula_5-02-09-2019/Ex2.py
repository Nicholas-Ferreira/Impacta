
competicao = {}
for c in range(5):
    corredor = input('Corredor: ')

    voltas = []
    for v in range(4):
        volta = float(input('Tempo volta: '))
        voltas.append(volta)
    
    competicao[corredor] = voltas

for competidor in competicao:
    competicao[competidor] = sum(competicao[competidor]) / len(competicao[competidor])

print(min(competicao, key=competicao.get))