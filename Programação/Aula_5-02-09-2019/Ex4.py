arquivo = open(file="HarryPotter.txt", mode="r", encoding="utf8") 
s = arquivo.read()
lista = s.split()

palavras = {}
for palavra in lista:
    if palavra in palavras:
        palavras[palavra] += 1
    else:
        palavras[palavra] = 1

tupla = (max(palavras, key=palavras.get), palavras[max(palavras, key=palavras.get)])
print(tupla)