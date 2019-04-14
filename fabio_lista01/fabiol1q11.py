# entrada
tresdig = int(input('digite um numero de tres digitos: '))

# processamento
milhar = tresdig//100
dezena = tresdig%100//10 * 10
unidad = tresdig%10 * 100

inverso = unidad + dezena + milhar

# saida
print('o inverso de {} eh {}'.format(tresdig, inverso))
