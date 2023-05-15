# https://www.cnnbrasil.com.br/perguntas-frequentes/eleicoes/titulo-de-eleitor/quem-pode-votar-no-brasil/

# Sua missão: receber dados de uma pessoa, e dizer se o voto é
# OBRIGATORIO, FACULTATIVO ou NAO PERMITIDO

# Os dados da pessoa: idade, número inteiro em anos
# Alfabetizado(a): string, com os possiveis valores "SIM" ou "NAO"
alfa = input("Cidadão alfabetizado? ")
idade = int(input("Qual a idade? "))

alfa = alfa.upper()

if(alfa != 'SIM' and alfa != 'NAO'):
    print("valor invalído para alfabetização, por favor digite SIM ou NAO")
if(idade >= 18 and idade < 70 and alfa == 'sim'):
    print("Obrigatório")

elif(idade >= 16 and alfa == 'não'):
    print("Facultativo")
elif((idade >= 16 and idade < 18) or idade > 70):
    print("Facultativo")
else:
    print("Não permitido")

# Suas ferramentas:
# * if, elif, else, and e or
# * converter string para numero:
# a = input("digite o ano") resulta uma string, um texto, como "1984"
# a = int(input("digite o ano")) um número, como 1984
# * comparar valores


# Desafio 1: aceite "Sim", "sim" como valores para alfabetizado
# Desafio 2: Reclame se o usuário digitar algo diferente de "sim" e "nao",
# mas aceitando as variações de maiúscula e minúscula
