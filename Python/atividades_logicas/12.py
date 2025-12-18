"""Faça um algoritmo que leia o preço de um produto e mostre sseu novo preço, com 5% de desconto."""

print("Estamos com um desconto de 5% em qualquer produto")

produto = float(input("Qual o preço do produto? R$"))

desconto = produto * 0.05

novo_valor = produto - desconto

print("O produto que custava {:.2f}, agora custará {:.2f}".format(produto, novo_valor))
