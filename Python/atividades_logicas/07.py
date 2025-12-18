"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

nota = n1 + n2
media = nota / 2

print('A soma da sua nota é {} e sua média {}. '.format(nota, media))