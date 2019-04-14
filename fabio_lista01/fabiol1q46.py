# entrada
valor = float(input('valor do produto:'))

# processamento
parc = valor // 3
resto = valor % 3
entrada = parc + resto

# saida
print('entrada de {} R$ e duas prestacoes de {} R$'.format(entrada, parc))
