# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o valor do seu salário:'))
a = s*15/100
print('Você ganhou um aumento de 15% seu salário passou de {:.2f}R$ para {:.2f}R$'.format(s, s+a))
