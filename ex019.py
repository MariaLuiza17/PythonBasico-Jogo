# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a1 = str(input('1º aluno:'))
a2 = str(input('2º aluno:'))
a3 = str(input('3º aluno:'))
a4 = str(input('4º aluno:'))
lista = [a1, a2, a3, a4]
sorteio = choice(lista)

print('O aluno sorteado foi: {}'.format(sorteio))
