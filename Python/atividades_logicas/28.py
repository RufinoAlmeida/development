"""Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu"""

import random
import time

print("+" * 55)
print("Vou pensar em um número e você deve tentar adivinhar")
print("+" * 55)


print("PROCESSANDO...")
time.sleep(3)
numero = random.randint(0, 5)
print('Pronto!')
adivinhar = int(input("Em qual numero eu pensei? "))

if numero == adivinhar:
    print(f"Parabens você acertou eu pensei no numero {numero}")
else:
    print(f"Você errou, eu pensei no numero {numero}")