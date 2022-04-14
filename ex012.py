# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: R$'))
d = p*5/100
print('{}R$ - 5% de desconto = {}R$'.format(p, p-d))