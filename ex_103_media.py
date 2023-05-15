'''
Dada uma lista de alturas, indique a altura média
'''

alturas = [1.78, 1.56, 1.50, 1.8, 2.1, 1.7]

soma = 0
for altura in alturas:
    soma = soma + altura
    print("A soma atual é", soma, "A altura somada", altura)

print("media das alturas", soma/len(alturas))
print("tamanho da lista", len(alturas))