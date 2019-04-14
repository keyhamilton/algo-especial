# entrada
nota1 = int(input('digite a primeira nota: '))
peso1 = int(input('digite o peso da primeira nota: '))
nota2 = int(input('digite a segunda nota: '))
peso2 = int(input('digite o peso da segunda nota: '))
nota3 = int(input('digite a terceira nota: '))
peso3 = int(input('digite o peso da terceira nota: '))

# processamento
nota_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# saida
print('A media ponderada das notas {}, {} e {} eh {:.2f}'.format(nota1, nota2, nota3, nota_ponderada))

