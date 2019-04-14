# entrada
anos = int(input('idade em anos: '))
meses = int(input('e meses: '))
dias = int(input('e dias: '))

# processamento
idade = anos*365 + meses*30 + dias

# saida
print('A idade de {} anos, {} meses e {} dias equivale a {} dias'.format(anos, meses, dias, idade))
