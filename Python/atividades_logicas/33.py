'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 == n2 == n3:
    print('Todos os três números são iguais.')
else:
    print(f'O maior valor é: {max(n1, n2, n3)}')
    print(f'O menor valor é: {min(n1, n2, n3)}')
