"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""

n1 = int(input("Digite um numero: "))

antecessor = n1-1
sucessor = n1+1

print('O antecessor do número {} é {} e seu sucessor é {}'.format(n1, antecessor, sucessor))