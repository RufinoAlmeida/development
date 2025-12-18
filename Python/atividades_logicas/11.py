"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²"""

largura = float(input("Qual a largura da sua pareda? "))
altura = float(input("Qual a altura da sua parede? "))

parede = largura * altura 

pintada = parede / 2

print("Sua parede tem uma dimensão de {:.2f}m², você precisará de {}l de tinta para pintar".format(parede, pintada))