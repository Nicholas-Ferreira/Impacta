# Nicholas Mota Ferreira RA: 1900953

def contavogais(texto):
    vogais = { 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0  }

    for letra in texto.lower():
        if letra in vogais:
            vogais[letra] += 1

    return vogais