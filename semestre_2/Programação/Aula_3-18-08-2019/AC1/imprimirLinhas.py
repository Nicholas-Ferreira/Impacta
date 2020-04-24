# Nicholas Mota Ferreira - RA: 1900953

def linhaSimples(n):
    for i in range(n):
        print('-', end='')
    print()

def linhaDupla(n):
    for i in range(n):
        print('=', end='')
    print()

def linha(simbolo, n):
    for i in range(n):
        print(simbolo, end='')
    print()