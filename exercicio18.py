#Requisista os lados do triângulo para o usuário
la = int(input('Lado A: '))
lb = int(input('Lado B: '))
lc = int(input('Lado C: '))

#Retorna um resultado com base nos valores
#Caso não forme um triângulo
if (la + lb) < lc:
    print(f'Os lados {la}, {lb} e {lc} não formam um triângulo')
else:
    #Caso forme um triângulo Equilátero
    if la == lb == lc:
        print(f'Os lados {la}, {lb} e {lc} formam um triângulo equilátero')

    #Caso forme um triângulo Isosceles
    elif la == lb != lc:
        print(f'Os lados {la}, {lb} e {lc} formam um triângulo isosceles')
    elif la == lc != lb:
        print(f'Os lados {la}, {lb} e {lc} formam um triângulo isosceles')
    elif lc == lb != la:
        print(f'Os lados {la}, {lb} e {lc} formam um triângulo isosceles')

    #Caso forme um triângulo Escaleno
    elif la != lb != lc:
        print(f'Os lados {la}, {lb} e {lc} formam um triângulo escaleno')