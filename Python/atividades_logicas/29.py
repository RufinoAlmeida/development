'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custa R$7,00 por cada km acima do limite.'''

velocidade = float(input("Qual foi sua velocidade? "))

permitida = 80

multa = (velocidade - permitida) * 7

if velocidade > permitida:
    print(f"Você foi multado em R${multa}. porque excedeu a velocidade permitida de 80km.")

else:
    print("Siga seu trajeto com cuidado")
    