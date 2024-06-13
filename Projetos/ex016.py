#Crie um problema que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

import math

num = float(input('Digite um número real (com casas decimais: )'))
print(f'O número {num} tem a parte inteira {math.floor(num)}')