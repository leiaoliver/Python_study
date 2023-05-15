
'''
Explicacao

Os proximos dois arquivos tem a ver com baralho.

A idéia é representar cada carta como uma string de 2 letras:
    as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
    os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
    
O J de ouros, por exemplo, é representado pela string 'Jo'. O ás de copas,
pela string 'Ac'
'''

'''
esreva um código que recebe um naipe de cartas ('o', que significa ouros,
'p', que significa paus, 'c' de copas ou 'e' de espadas) e produz 
uma lista com todas as cartas desse naipe.

Entao, se você receber 'c', deve retornar deve exibir uma lista com 13 cartas, 
o ás de copas representado pela string 'Ac', os números '2c','3c',...'10c'
e as figuras,  'Jc', 'Qc', 'Kc'.

Dica: para juntar duas strings, faça nova='a'+'b'
Dica: para transformar um numero n em string, faça str(n)
'''
cartas_sem_nipes = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def cartas_do_nipe(nipe):
    cartas = []
    for carta in cartas_sem_nipes:
        carta_ok = carta+nipe
        cartas.append(carta_ok)
    return cartas



'''
escreva um código que cria um baralho completo, com todas as 52 cartas
ela nao recebe nada e produz uma lista.
os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
O J de ouros, por exemplo, é representado pela string 'Jo'. 
Assim 'Jo' é um dos elementos que deve aparecer na lista
'''
def baralho():
    baralho = []
    for naipe in ['o', 'c', 'p', 'e']:
        pedaco_baralho = cartas_do_nipe(naipe)
        baralho = baralho + pedaco_baralho
    return baralho

print(baralho())