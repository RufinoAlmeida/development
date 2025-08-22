'''Escreva um programa que leia dois números inteiros e comapre-os mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Nõ existe valor maior, os dois são iguais'''

v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digite o segundo número: '))

if v1 > v2:
    print('O primeiro valor é maior')

elif v2 > v1:
    print('O segundo numero é o maior')

else:
    print('Os dois números são iguais')