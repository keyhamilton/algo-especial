# entrada
metros = int(input('valor em metros: '))

# processamento
kilometro = metros // 1000
metro = metros % 1000

# saida
print('{} metros corresponde a {} kilometro(s) e {} metro(s)'.format(metros, kilometro, metro))
