#Coleta os 3 valores do usuário
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

#Variável que armazena o valor intermedário
intermediario = 0

#Verifica qual é o valor intermediário e retorna pro usuário
#Número 1
if num2 > num1 > num3:
    intermediario = num1

elif num3 > num1 > num2:
    intermediario = num1

#Número 2
elif num1 > num2 > num3:
    intermediario = num2

elif num3 > num2 > num1:
    intermediario = num2    

#Número 3
else:
    intermediario = num3

#Retorna o número intemediário
print(f'Valor intermediário: {intermediario}')