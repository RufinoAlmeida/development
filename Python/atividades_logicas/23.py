"Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados (Unidade, dezena, centena e milhar)"

n = int(input("Digite um número: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f"Unidade: {u} ")
print(f"Dezena: {d} ")
print(f"Centana: {c} ")
print(f"Milhar: {m} ")