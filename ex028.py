# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
n = random.randint(0,5)
aposta = int(input('Tente descobrir em qual número o computador pensou entre 0 e 5: '))
print('-'*45)
if aposta == n:
    print('Parabéns você adivinhou! O computador pensou no número: {}'.format(n))
else:
    print('Tente de novo! O computador pensou no número {}'.format(n))