#                             29/04/25
import os
os.system("cls")

#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# # SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


#replace("valor1", "valor2") -> substitui o valor 1 pelo valor2, exemplo se quero escrever com virgula
#mas depois transformar em ".", só fazer 


#ATIVIDADE 1 

# nota1 = float(input("digite sua primeira nota: ").replace(".","."))
# nota2 = float(input("digite sua segunda nota: ").replace(".","."))

# media = (nota1 + nota2)/2

# if media < 5:
#     print("REPROVADO:",  media)
# elif media >= 5 and media < 7:
#     print("EM RECUPERAÇÃO:", media)
# else:
#     print("APROVADO:", media)

#:.2f -> formata para 2 casas decimais apenas no fsting




#ATIVIDADE 2

# peso = float(input("digite seu peso: ").replace(".","."))
# altura = float(input("digite sua altura: ").replace(".","."))
# imc = round(peso / (altura * altura),2)

# if imc < 17:
#     print("muito abaixo do peso")
# elif imc >= 17 and imc <= 18.49:
#     print("abaixo do peso")
# elif imc >= 18.5 and imc <= 24.99:
#     print("peso normal")
# elif imc >= 25 and imc <= 29.99:
#     print("acima do peso")
# elif imc >= 30 and imc <= 34.99:
#     print("obesidade I")
# elif imc >= 35 and imc <= 39.99:
#     print("obesidade II")
# else:
#     print("obesidade III")



#ATIVIDADE 2

print(r"""              #######                           
           ###      ###                        
         ###           ##                      
        ##              ###############        
       ##                   #       #####      
      ##                                ###    
     ##                                   ##   
    ##                   ##                ##  
    ##                   ##                 #  
   ##                    #                  #  
   ##   ##                                  #  
  ##  # #####                               ## 
  ## #########                              ###
  #  #########                              ###
  # ############                           ##  
  # ### ### ## ##                         ##   
  # ## ######## #                       ##     
  # ##  ####### ##   ##              ####      
  # ##  ####### ##    #           ####         
  # #######  ## ##     ####   #####            
   # ######  ## #          ####                
   ##  #######  ####      ###                  
    ##   ###   ######    ##                    
     ###     ###    #     ###                  
        ######     #########                   
                    ##     ##                  
                    #       ##                 
                    #        ##                
                   ##         ##               
                   #    ##     ##              
                  ##    ##      ##             
                  # #    #       ##            
                 ## #    ##      ##            
           ####  ## #     #      ##            
            ####### #     #      ##            
             ##  # #      #     ###   ###      
               ### #   #  #     ##  ### ##     
             ##  # ##  # ##   ##   ##    ##    
            ####  # #####     ##  ##     ##    
           ##  ####            ###       ##    
           ##   ##    #####     #     # ##     
            #        #    #            ##      
            #       ##    ##      ##   ##      
            ##       ##   ##        ####       
             ##       ## ##         ##         
             ##  ##    ##         ##           
              ## ## #  #       ####            
               ###  #####  #####               
                 #####  #####                  """ )

# print("AUTOCAR")
# salario = float(input("digite seu salario: "))



# if salario <= 2799.99:
#     print("salario sem reajuste:", salario)
#     print("percentual da sua faixa: 20%")
#     aumento = 0.20 * salario
#     print("aumento de: ", aumento )
#     total = aumento + salario
#     print("NOVO SALARIO: ", total)
# elif salario >= 2800 or salario <= 6999.99:
#     print("salario sem reajuste:", salario)
#     print("percentual da sua faixa: 15%")
#     aumento = 0.15 * salario
#     print("aumento de: ", aumento )
#     total = aumento + salario
#     print("NOVO SALARIO: ", total)
# elif salario >= 7000 or salario <= 14999.99:
#     print("salario sem reajuste:", salario)
#     print("percentual da sua faixa: 10%")
#     aumento = 0.10 * salario
#     print("aumento de: ", aumento )
#     total = aumento + salario
#     print("NOVO SALARIO: ", total)
# elif salario <= 15000:
#     print("salario sem reajuste:", salario)
#     print("percentual da sua faixa: 5%")
#     aumento = 0.05 * salario
#     print("aumento de: ", aumento )
#     total = aumento + salario
#     print("NOVO SALARIO: ", total)
