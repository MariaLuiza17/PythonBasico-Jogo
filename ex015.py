# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('''Aluguel de Carros
------------------''')

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias foi alugado? '))
pk = km*0.15
pd = dias*60
total = pk + pd

print('Preço por Km rodados: {:.2f}R$\nPreço por dias alugados: {}R$\nTotal: {:.2f}R$'.format(pk, pd, total))