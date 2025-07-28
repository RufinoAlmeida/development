nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
nota_3 = float(input('Digite sua terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3
print(f'A sua média foi {media:.1f}')

if media == 7.0:
    print('Você tirou uma boa nota. Parabens')

if media < 7.0:
    print('Você está de recuperação')

if media > 8:
    print('Sua nota foi incrivel')
