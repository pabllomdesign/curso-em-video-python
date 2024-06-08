#Solicite ao usuário dois números e exiba o produto deles.
preco_por_quilo = 7.99
print(f'Laranja | Preço por Kg: {preco_por_quilo}\n')

quantidade_comprada = float(input('Insira a quantidade: '))
total_pagar = quantidade_comprada*preco_por_quilo

print(f'\nTotal a pagar R${total_pagar:.2f}' )
