#Requisita o salário do usuário
salario = float(input('Salário: R$'))

#Coloca o valor do salário dentro dos limites do INSS
if salario > 8157.41:
    salario = 8157.41

#Retorna o valor do INSS

if salario <= 1518.00:
    print(f'INSS R${(salario * 0.075):.2f}')

elif 1518.00 < salario <= 2793.88:
    print(f'INSS R${(salario * 0.09 - 22.77):.2f}')

elif 2793.88 < salario <= 4190.83:
    print(f'INSS R${(salario * 0.12 - 106.59):.2f}')

elif salario > 4190.83:
    print(f'INSS R${(salario * 0.14 - 190.40):.2f}')


