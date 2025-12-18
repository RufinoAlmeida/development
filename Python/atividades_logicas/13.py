"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salaário, com 15% de aumento"""

salario = float(input("Qual seu salário? R$"))

aumento = salario * 0.15

novo_salario = salario + aumento

print("Seu salário era de R${:.2f}. Agora será de R${:.2f}".format(salario, novo_salario))