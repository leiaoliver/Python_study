# Sua missão: receber uma hora e um minuto, e dizer o valor do tempo atual e
# do tempo um minuto depois

# Se o usuário digitar uma hora maior ou igual a 24, ou um minuto maior ou igual a 60, reclame
# e NAO faça mais nada

# Exemplos: se o usuário digitar 10 para horas, 12 para minutos
# Imprimir:       Tempo atual: 10:12
#                Tempo futuro: 10:13

# Exemplos: se o usuário digitar 1 para horas, 59 para minutos
# Imprimir:       Tempo atual: 01:59
#                Tempo futuro: 02:00

# Exemplos: se o usuário digitar 23 para horas, 59 para minutos
# Imprimir:       Tempo atual: 23:59
#                Tempo futuro: 00:00

# Exemplos: se o usuário digitar 35 para horas, 59 para minutos
# Imprimir:      Valor invalido para horas

#Suas ferramentas:
# * operadores condicionais if/elif/else
# * para imprimir um número, podemos fazer assim
# h=12
# m=3
# print("O horário atual é {:02d}:{:02d}".format(h,m))
#note que já coloquei um código específico para garantir que um zero será adicionado na frente, mas apenas quando necessário

h = int(input("digite a hora: "))
m = int(input("digite o minuto: "))

if h > 23 or m > 59:
    print("algum input dado está incorreto")
else:
    print("tempo atual {:02d}:{:02d}".format(h,m))
novo_m = m+1
if novo_m > 59:
    novo_h = h+1
    novo_m = 0
else:
    novo_h = h
if novo_h > 23:
    novo_h = 0
print("Tempo futuro {:02d}:{:02d}".format(novo_h, novo_m))