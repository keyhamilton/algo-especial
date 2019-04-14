# entrada
numerador1 = int(input('1° numerador: '))
denominador1 = int(input('1° denominador: '))
numerador2 = int(input('2° numerador: '))
denominador2 = int(input('2° denominador: '))

# processamento
denominador_comum = denominador1 * denominador2
soma = (denominador_comum / denominador1 * numerador1) + (denominador_comum / denominador2 * numerador2)

# saida
print('A soma das fracoes {}/{} e {}/{} eh igual a {:.0f}/{}'.format(numerador1, denominador1, numerador2, denominador2, soma, denominador_comum))
