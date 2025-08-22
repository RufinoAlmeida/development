'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um trinângulo'''

a1 = float(input("Primeiro lado: "))
a2 = float(input("Segundo lado: "))
a3 = float(input("Terceiro lado: "))

soma = a1 + a3

if a1 < a2 + a3 and a2 + a1 + a3 and a3 < a1 + a2:
    print('Você formou um triangulo')

else:
    print('Isso não forma um triangulo')