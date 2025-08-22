'''Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome'''

nome = str(input("Digite seu nome: ")).strip()
nome_min = nome.upper()
print("SILVA" in nome_min)