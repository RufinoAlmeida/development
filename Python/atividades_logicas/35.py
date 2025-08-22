'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para saláarios superiores a R$1250,00 calcule um aumento de 10%. para os inferiores ou iguias, o aumento é de 15%.'''

s = float(input('Digite o valor do seu salário: '))

aumento1 = (s * 0.1) + s
aumento2 = (s * 0.15) + s

if s > 1250:
    print(f'Seu novo salário é {aumento1}')

else:
    print(f'Seu novo salário é {aumento2}')

