import os
os.system("cls")


#CONTINUAÇÃO INPUT COM INT E FLOAT
#int() -> converte para numero inteiro
#float() -> converte para numero quebrado

#exemplo 1
# numero = 10 
# numero2 = input("digite o numero: ")
# print("o tipo de numero é,", type(numero2))
# soma = numero + int(numero2)
# print(f"soma de {numero} + {numero2} = ", soma)

#exemplo 2
# num1 = input("digite um numero: ")
# soma = float(num1) + 15
# print("A soma de ",num1 , "+", "15" ,"=", soma)

#exemplo 3 -> MAIS PRÁTICA
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))
# soma = n1+n2
# print(f"a soma de {n1} + {n2} = ", soma)



#atividade 1

# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))
# multiplicação = n1*n2
# print(f"a multiplicação de {n1} * {n2} =", multiplicação)


# #atividade 2

# n1 = float(input("digite um numero: "))
# antecessor = n1-1
# print(f"o numero antecessor de {n1} = ", antecessor)
# sucessor = n1+1
# print(f"o sucessor de {n1} =", sucessor)


# #atividade 3

# n1 = float(input("digite o ano de nascimento: "))
# idade = 2025-n1
# print(f"sua idade é = ", idade)



#PORCENTAGEM
# print("25% de 100 = ", 0.25 * 100)
# print("4% de 400 =" 0.04 * 400)
# print("99% de 1525 = ", 0.99 * 1525)

#supondo que um produto custa 150 rs 
#e o caixa deu um desconto 15%




# Escreva um programa em python que leia 2 itens de um supermecado você deve armazenar
# o nome do valor do item, no final aplique 10% de desconto no primeiro tem 25% de desconto 
# no segundo item. Calcule o valor total da compra e mostre o nome e o valor com desconto de cada item.

print("===MERCADO===")
nome1 = (input("digite o nome do item1: "))
preco1 = float(input("digite o preco do item1: "))
nome2 = (input("digite o nome do item2: "))
preco2 = float(input("digite o preco do item2: "))

print("===CAIXA===")
desconto1 = 0.10 * preco1 
valor1 = round(preco1 - desconto1)
print(f"valor final item 1: {valor1}")

desconto2 = 0.25 * preco2 
valor2 = round(preco2 - desconto2)
print(f"valor final item 2: {valor2}")

print("-"*25)
valorfinal = valor2 + valor1
print(f"valor total: {valorfinal}")

#round (valor, quantidade de casas decimais) -> arredonda valores
