"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final.
de acordo com a média atingida:
Média abaixo de 5.0: Reprovado
Média entre 5.0 e 6.9: Recuperação
Médi 7.0 ou superior: Aprovado"""

class nota():
    nota1 = float(input("Qual é sua primeira nota? "))
    nota2 = float(input ("Qual é a sua segunda nota? "))

    media = (nota1 + nota2) / 2

    if media < 5:
        print("Você foi reprovado")
    
    if media == 5 or media < 7:
        print("você está de recuperação")
    
    else:
        print("Você está aprovado, parabéns")


    