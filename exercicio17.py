#Requisista os 3 lados do triângulo
a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

#Verifica se os números podem formar um triângulo
if (a + b) < c:
    print(f'Os lados {a}, {b} e {c} não formam um triângulo.')
else:
    print(f'Os ladors {a}, {b} e {c} formam um triângulo.')