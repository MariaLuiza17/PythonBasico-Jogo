# Faça um programa que leia algo pelo teclado e mostre na tela:
# O seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite qualquer coisa:')
print(type(a))
print('É numérico?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em letras maiúsculas?', a.isupper())
print('Está em letras minúsculas?', a.islower())