"Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar"

carteira = float(input("Quanto de dinheiro vocÊ tem na carteira? R$"))

dolar = 5.30

Converte = carteira / dolar

print("Com R${:.2f} você consegue comprar U${:.2f}".format(carteira, Converte))