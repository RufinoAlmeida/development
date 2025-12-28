"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento dos atletas
e mostre sua categoria, de acordo com a idade:

Até 9 anos: Mirim
Até 14 anos: Infantil 
Até 19 anos: Junior
Até 25 anos: Sênior
Acima: Master"""

from datetime import date

hoje = date.today()
ano_atual = hoje.year

nascimento = int(input("Em que ano você nasceu: "))

idade = ano_atual - nascimento

if idade <= 9:
    print("Você é categoria Mirim")

elif idade > 9 and idade <= 14:
    print("Você é categoria Infantil")

elif idade > 14 and idade <= 19:
    print("Você é categoria Junior")

elif idade > 19 and idade <= 25:
    print(" Você é categoria Sênior")

else:
    print("Você é categoria Master")