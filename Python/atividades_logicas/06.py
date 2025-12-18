"""Crei um algoritmo que leia um númnero e mostre o seu dobro, triplo e raiz quadrada"""

import math

n1 = int(input("Digite um número: "))

dobro = n1 * 2
triplo = n1 * 3
raiz = math.sqrt(n1)

print("O número digitado foi o {}".format(n1))
print("Seu dobro é {}\n" 
"Seu triplo {}\n" 
"Sua raiz quadrada é {:.3f}. ".format(dobro, triplo, raiz))