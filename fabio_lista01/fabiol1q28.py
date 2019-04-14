# entrada
horas = int(input('valor em horas: '))

# processamento
semana = horas // (24 * 7)
dia = horas % (24 * 7) // 24
hora = horas % 24

# saida
print('{} horas equivale a {} semana(s) {} dia(s) e {} hora(s)'.format(horas, semana, dia, hora))
