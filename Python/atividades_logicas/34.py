"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%."""

salario = float(input('Qual seu salário? R$'))



if salario > 1250:
    aumento = salario + (salario * 0,1)
    print('Seu salário agora é {}'.format(aumento))

else:
    aumento2 = salario + (salario * 0,15)
    print('Seu salário agora é {}'.format(aumento2))