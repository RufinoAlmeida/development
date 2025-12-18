"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa"""

cateto_o = float(input("Digite o valor do cateto oposto: "))
cateto_a = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = (cateto_o ** 2 + cateto_a ** 2) ** (1/2)

'Você pode usar a biblioteca math.hypot'

print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))