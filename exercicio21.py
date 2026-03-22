#Requisita o salário do usuário
salario = float(input('Salário: R$'))

#Variáveis que armazenam cada valor
INSS = 0
IR = 0
salario_liquido = 0

#Retorna o INSS

INSS = salario

#Limita o valor do INSS
if INSS > 8157.41:
    INSS = 8157.41

#Armazena o valor do INSS
if INSS <= 1518.00:
    INSS = INSS * 0.075

elif 1518.00 < INSS <= 2793.88:
    INSS = INSS * 0.09 - 22.77

elif 2793.88 < INSS <= 4190.83:
    INSS = INSS * 0.12 - 106.59

elif INSS > 4190.83:
    INSS = INSS * 0.14 - 190.40

#Retorna o IR

IR = salario

#Armazena o valor do IR
if IR <= 2259.2:
    IR = 0

elif 2259.2 < IR <= 2826.65:
    IR = IR * 0.075 - 169.44

elif 2826.65 < IR <= 3751.05:
    IR = IR * 0.15 - 381.44

elif 3751.05 < IR <= 4664.68:
    IR = IR * 0.225 - 662.77

else:
    IR = IR * 0.275 - 896

#Armazena o valor do salário líquido
salario_liquido = salario - (IR + INSS)

#Retorna pro usuário todos os valores
print(f'{'Salário':.<17}: R$ {salario:.2f}')
print(f'{'INSS':.<17}: R$ {INSS:.2f}')
print(f'{'IR':.<17}: R$ {IR:.2f}')
print(f'{'Salário Líquido':.<17}: R$ {salario_liquido:.2f}')