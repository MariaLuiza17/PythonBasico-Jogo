# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

a = float(input('Altura da parede:'))
l = float(input('Largura da parede:'))
area = a * l
tinta = area/2
print('Área da parede: {}m²'.format(area))
print('Tinta necessária para pintar a parede: {} litros'.format(tinta))
