# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

n = str(input('Digite seu nome:')).strip().lower()
print('Tem SILVA nesse nome? {}'.format('silva' in n))
