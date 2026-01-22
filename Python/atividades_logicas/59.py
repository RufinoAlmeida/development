"""Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
necessários para vencer."""

from random import randint
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(('Mais.. Tente mais um vez.'))
        elif jogador > computador:
            print('Tente mais um vez')
print('Acertou {}'.format(palpites))