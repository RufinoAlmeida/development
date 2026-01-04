"""Crie um programa que leia o ano de nascimento de sete pesssoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já saõ maiores"""
from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('{}º Pessoa em qual ano você nasceu? '.format(c)))
    idade = ano_atual - ano
    if idade >= 18:
        maior +=1
    else:
        menor +=1

print("Você tem {} pessoas maiores de idade".format(maior))
print("Você tem {} pessoas menores de idade".format(menor))


   