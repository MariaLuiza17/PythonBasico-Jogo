# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

c = str(input('Em que cidade você nasceu? ')).upper().strip()
print('Essa cidade começa com SANTO? {}'.format(c[:5] == 'SANTO'))