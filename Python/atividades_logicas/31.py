'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobtando R$0,50 por Km para viagens de até 200km
e R$0,45 para viagens mais longas.'''

print("====TABELA DE PREÇO DE DISTÂNCIA====")

print("ATÉ 200KM É COBRADO R$0,50 POR KM.\nACIMA DE 200KM É COBRADO R$0,45.")

viagem = int(input('Qual foi a distância da sua viagem: '))

if viagem <= 200:
    p1 = viagem * 0.50
    print(f"Sua viagem custou {p1}")

else:
    p2 = viagem * 0.45
    print(f'Sua viagem custou {p2}')