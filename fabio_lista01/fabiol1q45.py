# entrada
din = int(input('valor do saque:'))

# processamento
n50 = din//50
n10 = din%50//10
n5 = din%50%10//5
n1 = din%50%10%5

# saida
print('{} nota(s) 50 R$, {} nota(s) de 10 R$, {} nota(s) de 5 R$ e {} nota(s) de 1 R$'.format(n50, n10, n5, n1))
