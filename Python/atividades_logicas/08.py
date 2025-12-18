"""Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros"""

n1 = float(input("Digite um número: "))

cem = n1 * 100
mili = n1 * 1000

print('Seu número digitado foi {}, em centimetros é {} e em milimitros {}. '.format(n1, cem, mili))