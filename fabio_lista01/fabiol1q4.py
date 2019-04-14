# entrada
cotacao = float(input('valor da cotacao do dollar: '))
valor = float(input('valor em dollar para conversao: '))

# processamento
valor_reais = valor * cotacao

# saida
print('{:.2f} dolares equivale a {:.2f} reais'.format(valor, valor_reais))

