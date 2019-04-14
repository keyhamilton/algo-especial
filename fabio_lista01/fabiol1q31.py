# entrada
binario = int(input('digite um binario de 4 digitos: '))

# processamento
mil = binario // 1000
cem = binario % 1000 // 100
dez = binario % 1000 % 100 // 10
uni = binario % 10
decimal = mil * 2**3 + cem * 2**2 + dez * 2**1 + uni * 2**0

# saida
print('o binario {} equivale a {} em decimal'.format(binario, decimal))
