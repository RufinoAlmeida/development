"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado."""

print('Empréstimo para comigo')

casa = int(input('Qual o valor da casa que você quer comprar? '))
salario = int(input('Qual é seu salario? '))
tempo = int(input('Em quantos anos você pensa em quitar a casa? '))

parcela_total = casa / (tempo * 12)

parcela_1 = parcela_total * 0.3

if parcela_1 > salario:
    print('Infezlimente não podemos conceder o emprestimo, a parcela é 30% do seu salario')
    print('Sua parcela seria de R${:.2f}'.format(parcela_1))

else:
    print('Seu imprestimo será concedido ')
    print('Sua parcela será de R${:.2f}'.format(parcela_1))