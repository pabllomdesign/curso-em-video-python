#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e mostre o comprimento da hipotenusa.

import math 

catetoop = float(input('Insira o comprimento do cateto oposto: '))
catetoad = float(input('Insira o comprimento do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(catetoop, 2) + math.pow(catetoad,2))

print(f'O comprimento do cateto oposto é: {catetoop}')
print(f'O comprimento do cateto adjacente é:{catetoad}')
print(f'O compimrnento da hipotenusa é:{hipotenusa}')