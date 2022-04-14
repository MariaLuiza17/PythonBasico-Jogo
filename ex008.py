# Escreva um programa qque leia um valor em metros e o exiba convertido em cm e mm.

m = float(input('Digite um valor em metros:'))
print('{:.0f}m >>> {:.0f}cm >>> {:.0f}mm'.format(m, m*100, m*1000))