"Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido"

import random

alunos = []

while True:
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

    continuar = input("Deseja adicionar outro aluno? (sim/não): ")
    if continuar =="não":
        break

    if alunos:
        escolhido = random.choice(alunos)
        print(f"\n O aluno escolhido para apagar o quadro foi: {escolhido} ")
    else:
        print("Nenhum aluno foi adicionado.")