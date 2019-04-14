# entrada
a = int(input('A:'))
b = int(input('B:'))
c = int(input('C:'))
d = int(input('D:'))
e = int(input('E:'))
f = int(input('F:'))

# processamento
x = (c*e - b*f)/(a*e - b*d)
y = (a*f - c*d)/(a*e - b*d)

# saida
print('X = {} e Y = {}'.format(x, y))
