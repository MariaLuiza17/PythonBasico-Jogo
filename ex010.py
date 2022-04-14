# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

d = float(input('Quantos reais você tem na carteira? R$:'))
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(d, d/3.27))