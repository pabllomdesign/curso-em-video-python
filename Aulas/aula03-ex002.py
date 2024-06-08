#Solicite ao usuário dois números e exiba a diferença entre eles.
n1 = float(input('Informe o valor da compra: R$'))
n2 = float(input('Informe o valor recebido: R$'))
print(f'Troco a ser devolvido: R${n1 - n2:.2f}')