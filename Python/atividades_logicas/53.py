"""Crie um programa que leia uma frase ou palavra qualquer e diga
se ela é um palindromo, desconsiderando os espaços"""

frase = str(input('Digite uma frase ou palavra: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = ''
for l in range(len(juntar)- 1, -1, -1):
    inverso += juntar [l]
if inverso == juntar:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')