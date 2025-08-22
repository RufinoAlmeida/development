'''Crie um porgrama que leia o nome completo de uma pessoa e mostre: 
O nome com todas as letras maiúclas e minúsculas
Quantas letras ao todo (sem considerar espeçaos)
Qauntas letras tem o primeiro nome'''

nome = input("Digite seu nome completo: ")

maiusculo = nome.upper()
minuscula = nome.lower()
total_letras = len(nome.replace(" ", ""))
primeiro_nome = nome.split()[0]
letras_primeiro_nome = len(primeiro_nome)

print(maiusculo)
print(minuscula)
print(f"Seu primeiro nome tem {letras_primeiro_nome} letras.")
print(f"Seu nome tem {total_letras} letras.")