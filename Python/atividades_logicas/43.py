"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa calcule seu IMC e mostre seu status,
de acordo com a taela abaixo:
Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obseidade
Acima de 40: Obseidade móbida"""

altura = float(input("Qual é a sua altura? (ex: 1.83)? "))
peso = float(input("Qual é seu peso? "))

IMC = peso / (altura * altura)
IMC_formatado = float(f"{IMC:.2f}")

if IMC_formatado < 18.50:
    print("Está abaixo do peso")
elif IMC_formatado > 18.50 and IMC_formatado <=25:
    print("Está com o peso ideal")
elif IMC_formatado > 25 and IMC_formatado <=30:
    print('Está com sobrepeso')
elif IMC_formatado > 30 and IMC_formatado <=40:
    print('Está com obseidade')
else:
    print("Está com obseidade mórbida")