#Pede o valor da compra pro usuário
compra = float(input('Digite o valor da compra: R$'))

#Retorna o valor original pro usuário
print(f'Valor original: R${compra}')

#Retorna o valor com disconto com base no valor da compra
if compra>5000:
    print(f'Com desconto: R${compra - compra*0.075}')
else:
    print(f'Com desconto: R${compra - compra*0.035}')