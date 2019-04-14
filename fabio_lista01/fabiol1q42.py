# entrada
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

# processamento
dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# saida
print('distancia entre os pontos: {:.2f}'.format(dist))
