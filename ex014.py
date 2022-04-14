# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em ºC para converter em ºF: '))
f = 9 * c / 5 + 32
print(('{}ºC >>> {}ºF'.format(c, f)))