#Pede duas notas pro usuário
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#Calcula a média entre as notas
media = (nota1+nota2)/2

#Verifica se o usuário foi aprovado ou não e retorna o resultado
if media<6:
    print(f'Média {media} = Reprovado')
else:
    print(f'Média {media} = Aprovado')