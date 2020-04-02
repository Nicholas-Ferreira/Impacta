# Nicholas Mota Ferreira - RA: 1900953

def eh_primo(n):
    divisores = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            divisores += 1

    return divisores == 2