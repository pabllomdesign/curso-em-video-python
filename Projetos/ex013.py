#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salário, com aumento de 15%
import time

salario = float(input('Informe seu salário: R$'))
aumento_salario = (salario*15)/100
print('Calculando reajuste...')
time.sleep(1)
print(f'Seu salario atual é: R${salario:.2f} \nValor de aumento: R${aumento_salario:.2f} \nSeu novo salario é: R${salario + aumento_salario:.2f}')