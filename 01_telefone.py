# Sua missão: pedir ao usuário um ddd e um telefone, e verificar se os dados fornecidos
# são válidos.

# Consideraremos que um telefone válido tem 9 digitos e começa necessariamente por 9
# Assim, 
#* 988887733 é um telefone válido, 
#* 999888 não é, 
#* 899009988 não é
#* 9999999999 não é (10 numeros 9 seguidos, grande demais)
# (essa regra está obviamente errada, mas faz um exercicio interessante)

# Consideramos um ddd válido se ele tiver 2 digitos. Ou seja, se ele for maior ou igual a 10, e menor que 100

# Suas ferramentas:
# * input, para pedir texto ao usuário
# * converter string para numero:
# a = input("digite o ddd: ")      #resulta uma string, um texto, como "11"
# a = int(input("digite o ddd: ")) #um número, como 11
# * operadores de comparação
# if (a > 10):
#   print("o numero {} é maior que 10".format(a))

ddd = int(input("Digite o ddd do telefone: "))
telefone = int(input("Digite o número de telefone: "))

if (ddd < 10 or ddd > 100):
    print("ddd inválido")

elif (telefone < 900000000 or telefone > 999999999):
    print("telefone inválido")
else:
    print("telefone é valido")