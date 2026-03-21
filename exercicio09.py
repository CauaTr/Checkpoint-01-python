#Pede o primeiro valor para o usuário
num1 = float(input('Nota 1: '))

#Verifica se o primeiro número é válido
if 0 < num1 <= 10:

    #Coleta o segundo número
    num2 = float(input('Nota 2: '))

    #Verifica se o segundo número é válido
    if 0 < num2 <= 10:

        #Calcumla a média entre os números
        media = (num1 + num2) / 2

        #Retorna se o usuário foi aprovado ou reprovado com base na nota
        if media < 6:
            print(f'Média {media} - Reprovado')
        else:
            print(f'Média {media} - Aprovado')
    
    #Para o código se a nota 2 for inválida
    else:
        print(f'Nota {num2} é inválida!')
        
#Para o código se a nota 1 for inválida
else:
    print(f'Nota {num1} é inválida!')