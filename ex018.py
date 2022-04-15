# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o valor do ângulo:'))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Ângulo: {}\nSeno: {:.2f}\nCos: {:.2f}\nTangente: {:.2f}'.format(angulo, seno, cos, tangente))