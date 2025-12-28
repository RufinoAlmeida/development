"""Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

idade = int(input("Quantos anos vocÊ tem "))

faltam = 18 - idade

if idade == 18:
    print("Você é obrigado a se alistar nos serviços militares")

if idade == 16 < 18:
    print('Você tem a opção de se alistar ou esperar até fazer 18 anos')
    

if idade > 18:
    print('Entendemos que você já deve ser uma pessoa alsitada')

else:
    print('Você não tem idade para alistar')
    print('Ainda faltam {} para você se alistar obrigatóriamente'.format(faltam))