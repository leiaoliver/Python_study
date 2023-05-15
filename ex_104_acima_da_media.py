'''
Dada uma lista de alturas, produza uma segunda lista, com todas
as alturas que estão acima da média
'''

alturas = [1.78,1.56,1.50,1.8,2.1,1.7]

soma = 0
for altura in alturas:
    soma = soma + altura
    print("A soma atual é", soma, "A altura somada", altura)

media = soma/len(alturas)
print("media das alturas", soma/len(alturas))
print("tamanho da lista", len(alturas))

altos = []
for altura in alturas:
    if altura > media:
        altos.append(altura)
        print("adicionei", altura, "a lista ficou", altos)