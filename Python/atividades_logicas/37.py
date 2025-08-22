'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado'''

print('=' * 20)
print('EMPRÉSTIMO'.center(20))
print('=' * 20)

casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos vocÊ vai pagar essa casa? '))

parcelas = casa / (anos * 12)
regra = salario * 0.3

if parcelas > regra:
    print(f'O valor da prestação é R${parcelas:.2f}, com isso esse valor excede 30% do seu salário. O empréstimo foi negado')

else:
    print(f'O valor da parcela é R${parcelas:.2f}. Seu empréstimo foi aprovado')
