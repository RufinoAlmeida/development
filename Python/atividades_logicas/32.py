'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''

print('++++++Conceito de ano BISSEXTO: Um ano bissexto ocorre a cada quatro anos e tem 366 dias,'\
'com fevereiro tendo 29 dias.'\
'Isso acontece para corrigir o descompasso entre o calendário civil e o ano solar.'\
'A regra geral é que um ano é bissexto se for divisível por 4,'\
'mas anos centenários (terminados em 00)'\
'só são bissextos se forem divisíveis por 400.++++++')

from datetime import date
ano = int(input('Que ano quer analisar? Cloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0: #Tem que ser dividil por 4 e não por 100 ou por 400
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')