# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('Cateto oposto:'))
ca = float(input('Cateto adjacente:'))
h = hypot(co, ca) # ou (co ** 2 + ca ** 2) ** (1/2)
print('Hipotenusa: {:.2f}'.format(h))