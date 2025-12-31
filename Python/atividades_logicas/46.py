"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artificios, indo de 10 até 0, cin um pausa de 1 segundo entre eles."""

from time import sleep
print("FALTAM 10 SEGUNDOS PARA O ANO NOVO")

for cont in range(0, 11):
    print(cont)
    sleep(0.5)
print("FELIZ ANO NOVO!!!!")