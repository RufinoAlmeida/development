"Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu anteessor"

n1 = int(input("Digite um número? "))
ant = n1 - 1
suce = n1 + 1
print("O número digitado foi {}, e seu antecessor é {} e seu sucessor é {}".format(n1, ant, suce))