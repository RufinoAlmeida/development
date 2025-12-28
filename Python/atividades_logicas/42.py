r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segunfo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end="")

    if r1 == r2 == r3:
        print('Eqilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isóceles')

else: 
    print('Os segmentos acima não podem formar triângulo')