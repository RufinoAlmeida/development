'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR'''

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O numero {numero} é PAR.')

else:
    print(f'o numero {numero} é IMPAR')