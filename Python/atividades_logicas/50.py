"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
dqueles que forem pares. Se o valor digitado for impar, desconsidere-o"""

soma = 0
for digite in range(1, 7):
    digite = int(input('Digite {} numeros? '.format(digite)))
    if digite % 2 ==0:
        soma = soma + digite
2

print(soma)