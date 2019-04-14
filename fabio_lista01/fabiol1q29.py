# entrada
meses = int(input('valor em meses '))

# processamento
ano = meses // 12
mes = meses % 12

# saida
print('{} meses equivale a {} ano(s) e {} mes(es)'.format(meses, ano, mes))
