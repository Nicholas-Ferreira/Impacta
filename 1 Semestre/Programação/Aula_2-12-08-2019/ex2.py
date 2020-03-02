numeros = [i+1 for i in range(20)]

pares = [i for i in numeros if i % 2 == 0]
impares = [i for i in numeros if i % 2 == 1]

print(numeros)
print(pares, impares)