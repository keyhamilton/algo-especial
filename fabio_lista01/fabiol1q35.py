# entrada
num = int(input('digite um numero inteiro de 4 digitos: '))

# processamento
mil = num // 1000
cem = num % 1000 // 100
dez = num % 1000 % 100 // 10
uni = num % 10

soma = mil + cem + dez + uni

# saida
print('A soma dos algarismos de {} eh igual a {}'.format(num, soma))
