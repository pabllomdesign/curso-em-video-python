#Faça um algoritmo que leia a largura e altura de uma parede em metros. Calcule a sua área e a quantidade de tinta nescessaria para pinta-la. Considerando que a cada litro de tinta pinta uma área de 2m².

largura = float(input('Insira a largura da parede (em metros): '))
altura = float(input('Insira a altura da parede (em metros): '))
area = largura * altura

print(f'A parede tem: {area}m² e a quantidade de tinta necessária é de: {area/2} litros')