# entrada
minutos = int(input('valor em minutos: '))

# processamento
hora = minutos//60
minuto = minutos%60

# saida
print('{} minutos equivale a {}h e {}min'.format(minutos, hora, minuto))
