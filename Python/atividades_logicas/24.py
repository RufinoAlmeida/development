'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo'''

cid = str(input('Em que cidade você nasceu? ')).strip()
primeiro_nome = cid.split()[0]

if primeiro_nome.casefold() != 'Santo':
    print("O nome da sua cidade é muito bonito")

else:
    print(' primeiro nome digitado não tem Santo')