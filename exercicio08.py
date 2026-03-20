#Pede uma nota pro usuário
nota = float(input('Digite uma nota: '))

#Verifica se a nota está entre 0 e 10 e retorna a validade pro usuário
if 0<nota<=10:
    print(f'{nota} é uma nota válida')
else:
    print(f'{nota} é uma nota inválida')