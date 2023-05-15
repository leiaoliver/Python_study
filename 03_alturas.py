# Sua missão: receber três alturas de pessoas, e imprimir a média
# As alturas são números reais (como 2.12, ou 1.78)

# Suas ferramentas:
# * pedir um número real para o usuário
# a = input("digite um numero: ")          #a é um texto, como "1.78"
# a = float(input("digite um numero: "))   #a é um numero,como  1.78
# * somar numeros
# soma = a + 10 + 30
# * dividir
# media = soma/2
a1 = float(input("digite uma altura: "))
if a1 > 3:
    print("alerta! Possível dado inválido")
a2 = float(input("digite uma altura: "))
if a2 > 3:
    print("alerta! Possível dado inválido")
a3 = float(input("digite uma altura: "))
if a3 > 3:
    print("alerta! Possível dado inválido")

soma = a1+a2+a3
media = soma/3

print("a media da altura das pessoas é {:.2f}".format(media))
# Desafio: se algum dos números for absurdo (por exemplo, maior do que 3 metros), seu programa deve alertar
# o usuário da existência de um possivel dado inválido