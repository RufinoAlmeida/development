'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A".
Em que posição ele aparece a primeira vez.
Em que posição ela aparece a última vez'''

frase = str(input('Digite uma frase: ')).strip()
frase_minuscula = frase.casefold()
cont_a = frase_minuscula.count("a")
primeira = frase_minuscula.find("a")+1
ultima = frase_minuscula.rfind('a')+1

print(f'A letra "A" aparece {cont_a}')
print(f'A letra maiúscula ou minúscula aparece pela primeira vez na ocorrência {primeira}.')
print(f'A letra maiúscula ou minúscula aparece pela ultima vez na ocorrência {ultima}.')