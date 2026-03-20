#Pede um número pro usuário
numero = float(input('Digite um número: '))

#Verifica se o número é par ou ímpar
par_imp = numero % 2

#Retorna uma mensagem pro usuário com base no resultado de par_imp
#Par
if par_imp == 0:
    print(f'O número {numero} é par')

#Impar
else:
    print(f'O número {numero} é impar')