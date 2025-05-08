#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)

#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes forem FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições forem VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")


# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  
# if x > 1000:
#     print("verdade")
# else:
#     print("falso")


# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)


#ATIVIDADE 1

# idade = 18
# if int(input("digite sua idade: ")) >= idade:
#     print("MAIOR DE IDADE")
# else:
#     print("MENOR DE IDADE")


# #DESAFIO 2

# idade = int(input("digite sua idade: "))
# if idade >= 18 and idade <=120:
#     print("USUARIO AUTENTIFICADO")
# else:
#     if idade > 0 and idade <= 18:
#         print("USUARIO INVALIDO, MENOR DE IDADE")
#     else:
#         print("USUARIO INVALIDO, MAIOR DE IDADE")


#DESAFIO 2

# email = (input("digite seu e-mail: "))
# senha = int(input("digite sua senha: "))
# if email == "pthon@senai.com" and senha == 12345678:
#     print ("USUARIO AUTENTICADO")
# else:
#     print ("USUARIO OU SENHA INVALIDO")


#DESAFIO 3: 
# se o cliente pedir menos que uma duzia
# será 0.30 se pedir uma duzia ou mais será 0.25

# print("="*20, "LOJA", "="*20)
# qnt= int(input("digite a quantidade de maças: "))
# if qnt < 12:
#     calculo = qnt * 0.30
#     print ("você ira pagar (R$0.30 unidade) R$: ", calculo)
# else:
#     calculo = qnt * 0.25
#     print ("você ira pagar (R$ 0.25 unidade) R$: ", calculo)





#                             29/04/25

#DESAFIO 1 indicar de a letra é maiuscula ou minuscula:

# letra = input("digite uma letra:")

# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
#     print("essa letra é uma vogal:", letra) 
# else:
#     print("essa letra é uma consoante:", letra)



#FUNCÕES NOVAS:
#upper() -> CONVERTER TUDO PARA MAIUSCULO
#lower() -> CONVERTER TUDO PARA MINUSCULO



#EXEMPLO MESMA ATIVIDADE 1 POREM USANDO O LOWER:

# letra = input("digite uma letra:"). lower()
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"
#     print("essa letra é uma vogal:", letra) 
# else:
#     print("essa letra é uma consoante:", letra)



#DESAFIO 2 indicar se um numero é maior ou menor que o outro:
 
# numero1 = float(input("digite um numero: "))
# numero2 = float(input("digite outro numero: "))

# if numero1 > numero2:
#     print("numero maior: ", numero1 )
#     print("numero menor: ", numero2)
# else:
#     print("numero maior: ", numero2)
#     print("numero menor: ", numero1)
