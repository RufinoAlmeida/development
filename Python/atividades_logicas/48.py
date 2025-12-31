"""Faça um programa que calcule a soma entre todos os números imapres que são múltiplos de trÊs
e que se encontram no intervalo de 1 até 500."""
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 ==0:
        cont = cont + 1
        soma = soma + n
        
print(soma)
print(cont)