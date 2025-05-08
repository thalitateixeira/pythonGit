import os
os.system("cls")

#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versao 3.10)
#math valor:
#   case valor:

#EX 1:

# linguagem = 10

# match linguagem:
    
#     case "python":
#         print("é facil")
#     case "java":
#         print("muito codigo, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("nao dorme")
#     case 10:
#         print("entrou aqui")
#     case _ :
#         print("outro caso")



#EX 2:

# semana = int(input("digite o numero de 1 a 7:"))

# match semana:
#     case 1:
#         print("segunda")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")
#     case _ :
#         print("eu disse de 1 a 7 ta")




#atividade 1

# print(r"""

#  1- IPHONE 15: R$ 5000,00
#  2- XIAOMI REDMI 13 PRO PLUS: R$ 2500,00
#  3- SAMSUNG S25 265GB: R$ 6999,99

# FRETE: 
# SP: 10,00
# MG: 15,00
# RS: 20,00

# """)

# produto = (input("digite o numero do produto:"))
# estado = (input("digite a sigla do estado: ").upper())

# print("="*20)

# preco = 0
# frete = 0

# match estado:
#     case "SP":
#         frete = 10
#     case "MG":
#         frete = 15
#     case "RS":
#         frete = 20

# match produto:
#     case "1":
#         preco = 5000
#     case "2":
#         preco = 2500
#     case "3":
#         preco = 6999

# print("preço R$:", preco)
# print("frete R$:", frete)
# print("valor total R$:", preco + frete)



# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")



#ATIVIDADE DA PEDRA PAPEL TESOURA (MEU)

# print("JOGO PEDRA PAPEL TESOURA")

# jogador = input("digite pedra papel ou tesoura:")
# import random
# maquina = random.randint(1,3)

# papel = """ PAPEL
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """ PEDRA
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """ TESOURA
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """
# match maquina:
#     case 1 :
#         maquina = pedra 
#     case 2:
#         maquina = papel
#     case 3:
#         maquina = tesoura

# match jogador:
#     case "pedra":
#         jogador = pedra
#     case "papel":
#         jogador = papel
#     case "tesoura":
#         jogador = tesoura

# print("VOCÊ ESCOLHEU:", jogador)
# print("MAQUINA ESCOLHEU:", maquina)

# match jogador: 
#     case _ if jogador == pedra and maquina == pedra:
#         print("empate")
#     case _ if jogador == pedra and maquina == papel:
#         print("jogador perdeu")
#     case _ if jogador == pedra and maquina == tesoura:
#         print("jogador venceu")
#     case _ if jogador == papel and maquina == papel:
#         print("empate")
#     case _ if jogador == papel and maquina == pedra:
#         print("jogador venceu")
#     case _ if jogador == papel and maquina == tesoura:
#         print("jogador perdeu")
#     case _ if jogador == tesoura and maquina == tesoura:
#         print("empate")
#     case _ if jogador == tesoura and maquina == pedra:
#         print("jogador perdeu")
#     case _ if jogador == tesoura and maquina == papel:
#         print("jogador venceu")








# #ATIVIDADE PEDRA PAPEL TESOURA (PROFESSOR)
# print("2 MODO - PEDRA PAPEL TESOURA")


# print("JOGO PEDRA PAPEL TESOURA ")

# papel = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

# #pedra=1 papel=2 tesoura=3
# mao = input("Digite pedra ou papel ou tesoura :")
# maquina = random.randint(1,3)

# match maquina :
#     case 1:
#         maquina = "pedra"
#     case 2:
#         maquina = "papel"
#     case 3 :
#         maquina ="tesoura"

# match mao:

#     case _ if mao== "pedra" and maquina=="pedra" :
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {pedra}")
#         print("EMPATOU!")
    
#     case _ if mao== "pedra" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {pedra}")
#         print("PERDEU!")
#     case _ if mao== "pedra" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {pedra}")
#         print("GANHOU!")
#     case _ if mao== "papel" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {papel}")
#         print("EMPATOU!")
#     case _ if mao== "papel" and maquina=="pedra":
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {papel}")
#         print("GANHOU")
#     case _ if mao== "papel" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {papel}")
#         print("PERDEU!")
#     case _ if mao== "tesoura" and maquina=="pedra":
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {tesoura}")
#         print("PERDEU!")
#     case _ if mao== "tesoura" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {tesoura}")
#         print("GANHOU!")
#     case _ if mao== "tesoura" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {tesoura}")
#         print("EMPATOU!")
#     case _:
#         print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")



