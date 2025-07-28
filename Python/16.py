"Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira"

from math import trunc

n = float(input("Digite um número: "))

parte_inteira = trunc(n)

print("A parte inteira de {} é {}".format(n, parte_inteira))