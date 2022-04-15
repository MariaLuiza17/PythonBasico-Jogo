# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo:'))

print(nome.upper())
print(nome.lower())
print('-'*30)
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
n = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(n[0])))
