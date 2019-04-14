# entrada
segundos = int(input('valor em segundos: '))

# processamento
hora = segundos // 3600
minuto = segundos % 3600 // 60
segundo = segundos % 60

# saida
print('{} segundos equivale a {}h {}min {}s'.format(segundos, hora, minuto, segundo))
