#Calculando a media de alunos
nome = input('Nome do aluno: ')
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))
resultado = (nota1 + nota2 + nota3 + nota4) / 4

print(f'{nome}, sua nota final é: {resultado:.2f}')
