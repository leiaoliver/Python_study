'''
Dada uma lista de preços, descobrir qual o maior dentre eles
'''

precos = [100,45,78,9,200,13,300,2]

i = 0
preco_maior_ate_agr = precos[i]

#while
while i < len(precos):
    preco_desse_indice = precos[i]
    if preco_maior_ate_agr < preco_desse_indice:
        preco_maior_ate_agr = preco_desse_indice
    print("preço maior", preco_maior_ate_agr, "preço visto agora", preco_desse_indice)
    i = i + 1


#for
for preco_desse_indice in precos:
    if preco_maior_ate_agr < preco_desse_indice:
        preco_maior_ate_agr = preco_desse_indice
    print("preço maior", preco_maior_ate_agr, "preço visto agora", preco_desse_indice)

