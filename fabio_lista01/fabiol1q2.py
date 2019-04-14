# entrada
hora = int(input('valor em horas: '))
minuto = int(input('valor em minutos: '))

# processamento
total_minutos = hora * 60 + minuto

# saida
print('{}h e {}min equivale a {} minutos'.format(hora, minuto, total_minutos))
