# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc

n = float(input('Digite qualquer número com decimal:'))
print('A porção inteira de {} é {}'.format(n, trunc(n))) # ou int(n)
