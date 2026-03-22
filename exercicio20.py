#Requisita o salário do usuário
salario = float(input('Salário: R$'))

#Retorna o valor do IR com base no salário
if salario <= 2259.2:
    print('Sem IR a ser pago')

elif 2259.2 < salario <= 2826.65:
    print(f'IR: R${(salario * 0.075 - 169.44):.2f}')

elif 2826.65 < salario <= 3751.05:
    print(f'IR: R${(salario * 0.15 - 381.44):.2f}')

elif 3751.05 < salario <= 4664.68:
    print(f'IR: R${(salario * 0.225 - 662.77):.2f}')

else:
    print(f'IR: R${(salario * 0.275 - 896):.2f}')