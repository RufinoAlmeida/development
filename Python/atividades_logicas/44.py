"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
Á vista dinheiro/cheque: 10% de desconto
Á vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros"""

print("FORMAS DE PAGAMENTOS")

print("[1] á vista dinheiro/cheque \n[2] á vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão")

compra = float(input("Qual o valor do produto? R$"))

forma_pay = int(input("Qual sua forma de pagamento? "))

um = compra - (compra * 0.10) # 10% de desconto
dois = compra - (compra * 0.05) # 5% de desconto
tres = compra # preço normal
quatro = compra + (compra * 0.2) # 20% de juros

if forma_pay == 1:
    print('O valor da sua compra será {:.2f}'.format(um))
elif forma_pay == 2:
    print('O valor da sua compra será {:.2f}'.format(dois))
elif forma_pay == 3:
    print('O valor da sua compra será {:.2f}'.format(tres))
elif forma_pay == 4:
    print('O valor da sua compra será {:.2f}'.format(quatro))
else:
    print('Essa opção não está disponivel. Retorne o processo novamente!')
