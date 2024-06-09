try:
  numero = int(input('Digite um número inteiro: '))
  print(f'Você digitou {numero}, seu sucessor {numero + 1} e seu antecessor é {numero - 1}')

except ValueError:
  print('Valor inválido!\nVerifique se o valor digitado é um número inteiro!')