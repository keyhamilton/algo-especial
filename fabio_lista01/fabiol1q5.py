# entrada
num = int(input('digite um numero de tres digitos: '))

#processamento
centena = num //100
dezena = num % 100 // 10
unidade = num % 100 % 10
soma = centena + dezena + unidade

# saida
print('a soma dos algarismos de {} equivale a {}'.format(num, soma))
