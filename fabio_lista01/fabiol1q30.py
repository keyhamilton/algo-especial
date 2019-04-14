# entrada
minutos = int(input('valor em minutos: '))

# processamento
dia = minutos // (60 * 24 * 7)
hora = minutos % ((60 * 24 * 7) // 60)
minuto = minutos % 60

# saida
print('{} minutos equivale a {} dia(s), {} hora(s) e {} minuto(s)'.format(minutos, dia, hora, minuto))
