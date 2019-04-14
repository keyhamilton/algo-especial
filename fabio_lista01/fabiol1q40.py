# entrada
ano = int(input('anos que fumou: '))
cdia = int(input('quantos cigarros por dia: '))
preco = float(input('preco da carteira: '))

# processamento
tcigar = ano * 365 * cdia
cart = tcigar//20 + (tcigar%20 + 19)//20
gasto = preco * cart

# saida
print('Fumando {} cigarro(s) por dia durante {} anos, gasta-se {} R$'.format(cdia, ano, gasto))
