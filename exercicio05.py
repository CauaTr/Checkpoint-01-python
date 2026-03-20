#Pede um número pro usuário
numero = float(input('Digite um número: '))

#Verifica se o número é multiplo de 5
mult = numero % 5

print(f'O número digitado foi {numero}')

#Se o número não for múltiplo de 5, retorna o próximo múltiplo de 5
if mult>0:
    adicionar = 5-mult
    numero_mult = numero+adicionar
    print(f'O próximo número múltiplo de 5 será {numero_mult}')