#Pede 3 números pro usuário
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
num3 = float(input('Número 3: '))

#Variável do maior número
maior_num = 0

#Passa por todos os números e armazena o maior
if maior_num < num1:
    maior_num = num1

if maior_num < num2:
    maior_num = num2

if maior_num < num3:
    maior_num = num3

#Retorna o maior número
print(f'Maior valor: {maior_num}')