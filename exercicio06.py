#Pede 2 números pro usuário
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

#Verfica qual dos números é maior e retorna o maior pro usuário
if num1>num2:
    print(f'O maior número entre os digitados é {num1}')
else:
    print(f'O maior número entre os digitados é {num2}')