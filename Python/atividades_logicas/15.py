"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input("Quantos dias você alugará o carro? "))
km = int(input("Quantos Km você rodou com o carro? "))

valor_dia = dias * 60
valor_km = km * 1
total = valor_dia + valor_km

print("Valor total das diarias R${}".format(valor_dia))
print("Valor total dos Km rodados R${}".format(valor_km))
print("Você pagará pelo aluguel do carro um total de R${}".format(total))