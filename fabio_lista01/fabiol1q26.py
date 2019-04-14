# entrada
dias = int(input('numero de dias: '))

# processamento
semana = dias // 7
dia = dias % 7

# saida
print('{} dias corresponde a {} semana(s) e {} dia(s)'.format(dias, semana, dia))
