'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza primeiro nome = Ana último = Souza'''

nome = str(input('Digite seu nome: ')).strip()
primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

print(f'Seu primeiro nome é: {primeiro_nome} ')
print(f'Seu ultimo nome é: {ultimo_nome}')
