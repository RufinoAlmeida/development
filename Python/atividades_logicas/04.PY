"Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada"

n = int(input("Digite um número: "))

dobro = n * 2
triplo = n* 3
raiz = n ** 0.5

print("o valor digitado foi {}. \n Seu dobro é {}. \n Seu triplo é {}. \n Sua raiz quadrada é {:.2f} ".format(n, dobro, triplo, raiz))
