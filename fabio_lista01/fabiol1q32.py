# entrada
num = int(input('digite um numero inteiro de 3 digitos: '))

# processamento
centena = num // 100
dezena = num % 100 // 10
unidade = num % 10

inverso = unidade * 100 + dezena * 10 + centena
diferenca = num - inverso

# saida
print('A diferenca {}-{} eh igual a {}'.format(num, inverso, diferenca))
