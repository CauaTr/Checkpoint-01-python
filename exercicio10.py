#Pede o valor da compra
valor = float(input('Digite o valor da compra: R$'))

#Retorna um desconto com base no valor da compra
if valor>100:
    print('Você ganhou 10% de desconto!')
else:
    print('Você ganhou 5% de desconto!')