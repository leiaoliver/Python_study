'''
Dada uma lista de preços, indicando os preços de todos os itens consumidos em um restaurante,
produzir a soma total dos valores
'''

precos = [100, 45, 78, 9, 200, 13, 300, 2]

soma = 0
for preco in precos:
    soma = soma + preco
    print("a soma é", soma, "adicionei", preco)