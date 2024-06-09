#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias_alugado = int(input('Informe quantos dias alugado: '))
km_percorrido = float(input('Informa quantos km rodados: '))
diaria = (dias_alugado * 60) + (km_percorrido * 0.15)

print(f'Total do aluguel a pagar é: RS{diaria:.2f}')


