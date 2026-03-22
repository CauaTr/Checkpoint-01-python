#Pede o valor da compra pro usuário
valor = float(input('Digite o valor da compra: R$'))

#Pergunta a forma de pagamento
forma = int(input('1 - Pix\n2 - Dinheiro\n3 - Débito\n4 - Crédito\nQual será a forma de pagamento?: '))

#Retorna o valor original
print(f'Valor original: R${valor:.2f}')

#Retorna o preço ajustado com base na forma de pagamento
if forma == 1:
    print(f'Valor ajustado: R${(valor - valor * 0.05):.2f}')

elif forma == 2:
    print(f'Valor ajustado: R${valor:.2f}')

elif forma == 3:
    print(f'Valor ajustado: R${(valor + valor * 0.01):.2f}')

elif forma == 4:
    print(f'Valor ajustado: R${(valor + valor * 0.025):.2f}')

else:
    print('Forma de pagamento inválida')