"""Faça um programa que leiao peso de cinco pessoas. No final, mostre qual 
foi o maior e o menor peso lidos"""

pesos = []

for p in range(1, 8):
    peso = float(input('{}º Pessoa. Qual é seu peso: '.format(p)))
    pesos.append(peso)

print("A pessoa mais pesada tem o peso de {}Kg".format(max(pesos)))
print("A pessoa com o menor peso tem {}Kg".format(min(pesos)))