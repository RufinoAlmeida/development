"""Crie um programa que faça o computador jogar Jokenpô com você"""

import random
from time import sleep # Importa função para dar uma pausa dramática

print("=" * 20)
print("JOKENPÔ")
print("VOCÊ NÃO ME VENCE")
print("=" * 20)

print("[1] Pedra \n[2] Papel \n[3] Tesoura")

print("Eu já escolhi minha opção...")
jogador = int(input("Qual opção você escolhe (1, 2 ou 3): "))

# Validação simples para garantir que o número é válido
if jogador != 1 and jogador != 2 and jogador != 3:
    print("JOGADA INVÁLIDA! Tente novamente com 1, 2 ou 3.")
else:
    # Lógica do Computador
    computador = random.randint(1, 3)
    
    # Lista para transformar números em nomes (Estética)
    itens = ('Pedra', 'Papel', 'Tesoura')
    
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ!!!")
    
    print("-=" * 15)
    # Note que usamos [jogador - 1] porque listas começam no índice 0
    print(f"Computador jogou: {itens[computador - 1]}")
    print(f"Você jogou: {itens[jogador - 1]}")
    print("-=" * 15)

    # Lógica de Vencedor Simplificada
    if computador == jogador:
        print("EMPATE!")
    
    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        print("JOGADOR VENCEU!")
        
    else:
        print("COMPUTADOR VENCEU!")