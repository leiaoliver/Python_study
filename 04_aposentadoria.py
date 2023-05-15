# https://cmpprev.com.br/blog/idade-minima-para-aposentadoria-entenda-as-novas-regras/

# Sua missão: receber uma idade, um total de anos de contribuição, e o sexo, e responder se
# a pessoa já pode pedir a aposentadoria. (escrevendo "PODE" ou "NAO PODE")
# Consideraremos a regra para trabalhadores urbanos, descrita no link

# Detalhes: o sexo será enviado como "homem" ou "mulher"

# Suas ferramentas:
# * pedir um texto para o usuário
# a = input("digite o texto")
# * pedir um número inteiro para o usuário
# b = int(input("digite o número"))
# * operador logico or
#if (a == "mulher" or b > 10): #se a == "mulher", OU b > 10, não precisa ser os 2, o print ocorre
#    print ("pode 1")
# * operador logico and
#if (a == "mulher" and b > 10): #se a == "mulher", E b > 10, precisa ser os 2 ao mesmo tempo, o print ocorre
#    print ("pode 2")

# Desafio: Se o usuario escrever "Mulher", "MULHER" ou qualquer outro uso de maiúsculas, seu programa deve funcionar.
# Se escrever qualquer coisa que não seja "homem" nem "mulher", seu programa deve reclamar, e não imprimir
# nem "PODE" nem "NAO PODE"

idade = int(input("digite a idade: "))
tempo_contr = int(input("digite o tempo de contribuição: "))
sexo = input("digite o sexo do(a) segurado(a): ")

if tempo_contr < 15:
    print("NAO PODE")
elif idade < 62:
    print("NAO PODE")
elif idade < 65 and sexo == 'homem':
    print("NAO PODE")
else:
    print("PODE")