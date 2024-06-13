# Importa o módulo math, que contém funções matemáticas, como sqrt.
import math  

# Solicita ao usuário que digite um número, converte o valor de entrada para inteiro e o armazena na variável 'num'.
num = int(input('Digite um número: '))  

# Calcula a raiz quadrada do número armazenado em 'num' usando a função sqrt do módulo math e armazena o resultado na variável 'raiz'.
raiz = math.sqrt(num)  

# Exibe uma mensagem com o número original e sua raiz quadrada usando uma f-string para formatar a mensagem.
print(f'A raiz de {num} é igual a {raiz}')  
