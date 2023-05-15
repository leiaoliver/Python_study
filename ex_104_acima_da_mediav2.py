'''
Dada uma lista de alturas, produza uma segunda lista, com todas
as alturas que estão acima da média
'''

alturas = [1.78,1.56,1.50,1.8,2.1,1.7]

def soma_elementos(lista):
    soma = 0
    for altura in alturas:
        soma = soma + altura
        print("A soma atual é", soma, "A altura somada", altura)
    return soma

def media_elementos(lista):
    return soma_elementos(lista)/len(lista)

#print("media das alturas", media(lista))

def maiores_que_a_media(lista):
    media = media_elementos(lista)
    altos = []
    for altura in alturas:
        if altura > media:
            altos.append(altura)
            print("adicionei", altura, "a lista ficou", altos)
    return altos

print("media das alturas", maiores_que_a_media(alturas))