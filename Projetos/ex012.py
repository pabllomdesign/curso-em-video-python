#Faça um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto.
import time

produto = float(input('Informe o valor do produto: R$'))
desconto = (produto/100)*5

print('Calculando desconto, aguarde...')
time.sleep(2)

print('Pronto!')

time.sleep(1)

print(f'Seu desconto é de R${desconto:.2f}')
print(f'Total a pagar é: R${produto - desconto:.2f}')
