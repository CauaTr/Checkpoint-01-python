#Pede o salário pro usuário
salario = float(input('Salário-fixo: R$'))

#Pede as vendas do mês do usuário
vendas = int(input('Vendas do mês: '))

#Retorna o bônus do usuário com base nas vendas do mês
if vendas>100000:
    print(f'Bônus de R${(salario*2):.2f}')
else:
    print(f'Bônus de R${(salario*1.5):.2f}')