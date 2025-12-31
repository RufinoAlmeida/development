"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão"""

print("=" * 30)
print("10 PRIMEIROS TERMOS DESSA PA")
print("=" * 30)

pa = int(input('Digite uma número para mostra sua PA: '))
ra = int(input('Razão: '))
d = pa + (10 - 1) * ra
for n in range(pa, d + ra, ra):
    print('{}'.format(n), end=' > ')
print('FINALIZADO')
