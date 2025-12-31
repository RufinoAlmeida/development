"""Faça um programa que leia um número inteiro e diga se ele é pu não um número primo"""


num = int(input("Digite um número: "))

if num <= 1:
    print("NÃO É PRIMO")
else:
    eh_primo = True # Assumimos que é primo
    # Testamos do 2 até o número anterior
    for c in range(2, num):
        if num % c == 0:
            eh_primo = False # Achamos um divisor! Não é primo.
            break # Para o loop imediatamente (economiza processamento)
    
    if eh_primo:
        print("É PRIMO!")
    else:
        print("NÃO É PRIMO!")