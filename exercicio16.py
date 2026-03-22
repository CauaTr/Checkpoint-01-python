#Requisita 3 números pro usuário
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

#Variáveis que vão armazenar os números
maior = 0
intermediario = 0
menor = 0

#Analisa o número intermediário

if num2 > num1 > num3:
    intermediario = num1
elif num3 > num1 > num2:
    intermediario = num1

elif num1 > num2 > num3:
    intermediario = num2
elif num3 > num2 > num1:
    intermediario = num2

elif num2 > num3 > num1:
    intermediario = num3
elif num1 > num3 > num2:
    intermediario = num3

#Analisa o maior número
if maior < num1:
    maior = num1

if maior < num2:
    maior = num2

if maior < num3:
    maior = num3

#Analisa o menor número
menor = num1

if menor > num2:
    menor = num2

if menor > num3:
    menor = num3

#Retorna a ordem pro usuário
print(f'Ordem crescente {menor}, {intermediario} e {maior}')