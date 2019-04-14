# entrada
idade = int(input('valor em dias: '))

# processamento
anos = idade // 365
meses = idade % 365 // 30
dias = idade % 365 % 30 % 30

# saida
print('{} dias equivale a {} ano(s), {} mes(es) e {} dia(s)'.format(idade, anos, meses, dias))
