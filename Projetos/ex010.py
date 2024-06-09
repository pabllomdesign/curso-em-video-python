#Crie um algoritmo que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dóletas ela pode comprar

import time

dolar = float(input('Qual a cotação do dólar hoje: U$'))
din_carteira = float(input('Qual o valor que deseja converter: R$'))

print('Aguarde, estou convertendo...')
time.sleep(3)

print('Só mais um momento...')
time.sleep(2)

print('pronto...')
time.sleep(1)

print(f'Você pode sacar: u${din_carteira*dolar:.2f} Dólares')

