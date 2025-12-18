"""Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada"""


print("-" * 20)

print("TABUADA")

print("-" * 20)

n = int(input("Digite o número que você queira saber a tabuada? "))

for tabuada in range(1, 11):
    print(f"{n} x {tabuada} = {n * tabuada}")


print("-" * 20)